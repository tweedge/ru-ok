import argparse
import json
import pathlib
import requests
import time
from pprint import pprint

from torch import save

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


def parameters_builder(domain, bill_email):
    return {
        "definitions": [
            {
                "target": domain,
                "af": 4,
                "port": 443,
                "hostname": domain,
                "description": f"SSL measurement to {domain}",
                "resolve_on_probe": True,
                "skip_dns_check": True,
                "type": "sslcert",
            }
        ],
        "probes": [
            {
                "tags": {"include": [], "exclude": []},
                "type": "area",
                "value": "WW",
                "requested": 25,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "RU",
                "requested": 25,
            },
        ],
        "is_oneoff": True,
        "bill_to": bill_email,
    }


with open("targets.json") as targets_file:
    targets = json.load(targets_file)

measurements = {}

for domain, target_info in targets.items():
    backoff = 2
    time.sleep(backoff)
    while True:
        request = requests.post(
            f"https://atlas.ripe.net/api/v2/measurements//?key={args.ripe_atlas_key}",
            json=parameters_builder(domain, args.ripe_atlas_email),
        )
        if request.status_code == 201:
            response = request.json()
            if "measurements" in response.keys():
                print(f"Started measurements for {domain}")
                measurements[domain] = response["measurements"]
                break
            else:
                print(f"Request for {domain} measurement failed, no 'measurements' key in JSON response")
        else:
            print(f"Request for {domain} measurement failed, response code was {request.status_code} instead of 201")
        
        backoff = backoff * 2
        time.sleep(backoff)

        if backoff > 60:
            print(f"Failed to create measurement for {domain} too many times, skipping")
            break

print("Waiting fifteen minutes to ensure (under normal conditions) all results load")
time.sleep(900)

for domain, measurements in measurements.items():
    for measurement in measurements:
        backoff = 2
        time.sleep(backoff)
        while True:
            request = requests.get(
                f"https://atlas.ripe.net/api/v2/measurements/{measurement}/results/?format=json"
            )
            if request.status_code == 200:
                response = request.json()
                break
            else:
                print(f"Fail - response code was {request.status_code} instead of 200")
            
            backoff = backoff * 2
            time.sleep(backoff)

            if backoff > 60:
                print(f"Failed to retrieve results")
                break

        save_path = f"{args.output_folder}/{domain}/{measurement}/result.json"
        path = pathlib.Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(save_path, "w") as result_file:
            json.dump(response, result_file, indent=2)