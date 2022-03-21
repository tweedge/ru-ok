import argparse
import json
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

print("INFO: Saving measurements to measurements.tmp.json")
with open("measurements.tmp.json", "w") as status_file:
    json.dump(measurements, status_file, indent=2)

print(
    "Done. Please wait at least 15 minutes before harvesting results with collect_measurements.py"
)
