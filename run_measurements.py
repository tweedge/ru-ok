import argparse
import json
import pathlib
import random
import requests
import time
from pprint import pprint
from define_measurements import request_tcp_ping, request_ssl

parser = argparse.ArgumentParser(
    description="Runs measurements in RIPE ATLAS of SSL connectivity to targets in targets.json"
)
parser.add_argument(
    "--ripe-atlas-email",
    action="store",
    type=str,
    required=True,
    help="RIPE Atlas account email address",
)
parser.add_argument(
    "--ripe-atlas-key",
    action="store",
    type=str,
    required=True,
    help="RIPE Atlas APIv2 key, required to start measurements",
)
parser.add_argument(
    "--output-folder",
    action="store",
    type=str,
    required=True,
    help="Specifies output folder relative to the current working directory",
)
args = parser.parse_args()

with open("targets.json") as targets_file:
    targets = json.load(targets_file)

print("INFO: Building list of tasks from targets.json")
tasks = []
for target, definition in targets.items():
    if definition["test_type"] == "Webserver":
        tasks.append(
            {
                "id": f"{target}#HTTP",
                "target": target,
                "params": request_tcp_ping(target, args.ripe_atlas_email, 80),
            }
        )
        tasks.append(
            {
                "id": f"{target}#HTTPS",
                "target": target,
                "params": request_ssl(target, args.ripe_atlas_email),
            }
        )
    elif definition["test_type"] == "TCP on Ports":
        for port in definition["ports"]:
            tasks.append(
                {
                    "id": f"{target}#{port}",
                    "target": target,
                    "params": request_tcp_ping(target, args.ripe_atlas_email, port),
                }
            )
    else:
        print("FATAL: Not implemented, quitting")
        exit()

print(
    "INFO: Randomizing tasks to measure to more effectively sample if credits run out"
)
random.shuffle(tasks)
count_tasks = len(tasks)

print(f"INFO: Starting up to {count_tasks} measurements")
measurements = []
skip_remaining = False
finished = 0
for task in tasks:
    if not skip_remaining:
        backoff = 15
        time.sleep(backoff)
        while True:
            try:
                request = requests.post(
                    f"https://atlas.ripe.net/api/v2/measurements//?key={args.ripe_atlas_key}",
                    json=task["params"],
                )

                if request.status_code == 201:
                    response = request.json()
                    if "measurements" in response.keys():
                        finished += 1
                        print(
                            f"OK: Started task {finished}/{count_tasks} for {task['id']}"
                        )
                        measurements.append(
                            {"task": task, "measurement": response["measurements"]}
                        )
                        break
                    else:
                        print(
                            f"ERROR: Request for {task['id']} measurement failed, no 'measurements' key in JSON response"
                        )
                else:
                    print(
                        f"ERROR: Request for {task['id']} measurement failed, response code was {request.status_code} instead of 201"
                    )

            except Exception as e:
                print(f"ERROR: Silenced error '{e}'")

            backoff = backoff * 2
            time.sleep(backoff)

            if backoff > 1800:
                print(
                    f"FATAL: Failed to create measurement for {task['id']} too many times ..."
                )
                print(
                    "INFO: This script probably exceeded a RIPE Atlas limit and is now stopping collection."
                )
                skip_remaining = True
                break

print(
    "INFO: Saving measurements to measurements.tmp.json in case of result collection failure"
)
with open("measurements.tmp.json", "w") as status_file:
    json.dump(measurements, status_file, indent=2)

print(
    "INFO: Waiting fifteen minutes to ensure (under normal conditions) all results load"
)
time.sleep(900)

print("INFO: Beginning to fetch and enrich results ...")
probe_cache = {}
for measurement in measurements:
    target = measurement["task"]["target"]
    task_id = measurement["task"]["id"]
    measurement_id = measurement["measurement"][0]

    backoff = 2
    time.sleep(backoff)
    while True:
        try:
            request = requests.get(
                f"https://atlas.ripe.net/api/v2/measurements/{measurement_id}/results/?format=json"
            )

            if request.status_code == 200:
                response = request.json()
                print(
                    f"OK: Retrieved {len(response)} results from {task_id} measurement (#{measurement_id})"
                )
                break
            else:
                print(
                    f"ERROR: Couldn't retrieve results for measurement #{measurement_id}, response code was {request.status_code} instead of 200"
                )

        except Exception as e:
            print(f"ERROR: Silenced error '{e}'")

        backoff = backoff * 2
        time.sleep(backoff)

        if backoff > 600:
            print(
                f"FATAL: Failed to retrieve measurement data for #{measurement_id} too many times ..."
            )
            break

    updated_response = []
    for result in response:
        if result["prb_id"] in probe_cache.keys():
            print(f"Found probe ID {result['prb_id']} in cache")
            result["probe_data"] = probe_cache[result["prb_id"]]
        else:
            backoff = 0.5
            time.sleep(backoff)
            while True:
                try:
                    request = requests.get(
                        f"https://atlas.ripe.net/api/v2/probes/{result['prb_id']}/?format=json"
                    )

                    if request.status_code == 200:
                        response = request.json()
                        probe_cache[result["prb_id"]] = response
                        result["probe_data"] = response
                        print(
                            f"OK: Retrieved probe data for probe {result['prb_id']} and cached result"
                        )
                        break
                    else:
                        print(
                            f"ERROR: Couldn't retrieve probe metadata for {result['prb_id']}, code was {request.status_code} instead of 200"
                        )

                except Exception as e:
                    print(f"ERROR: Silenced error '{e}'")

                backoff = backoff * 2
                time.sleep(backoff)

                if backoff > 150:
                    print(
                        f"FATAL: Failed to retrieve probe metadata for probe {result['prb_id']} too many times"
                    )
                    break

        updated_response.append(result)

    save_path = f"{args.output_folder}/{target}/{measurement_id}/result.json"
    path = pathlib.Path(save_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    print(f"INFO: Saving enriched data to {save_path}")
    with open(save_path, "w") as result_file:
        json.dump(updated_response, result_file, indent=2)
