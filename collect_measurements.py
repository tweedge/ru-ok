import argparse
import json
import pathlib
import requests
import time

parser = argparse.ArgumentParser(
    description="Collects results of measurements from RIPE ATLAS which are present in measurements.tmp.json"
)
parser.add_argument(
    "--output-folder",
    action="store",
    type=str,
    required=True,
    help="Specifies output folder relative to the current working directory",
)
args = parser.parse_args()

print("INFO: Loading measurements.tmp.json to fetch prior results")
with open("measurements.tmp.json") as status_file:
    measurements = json.load(status_file)

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
            #print(f"Found probe ID {result['prb_id']} in cache")
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
