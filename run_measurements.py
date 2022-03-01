import argparse
import json
import pathlib
import random
import requests
import time
from pprint import pprint

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
            },
            {
                "target": domain,
                "af": 4,
                "timeout": 4000,
                "description": f'TCP "ping" measurement to {domain}',
                "protocol": "TCP",
                "resolve_on_probe": True,
                "packets": 3,
                "size": 0,
                "first_hop": 1,
                "max_hops": 32,
                "spread": 60,
                "port": 80,
                "paris": 16,
                "destination_option_size": 0,
                "hop_by_hop_option_size": 0,
                "dont_fragment": False,
                "skip_dns_check": True,
                "type": "traceroute",
            },
        ],
        "probes": [
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "RU",
                "requested": 10,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "BY",
                "requested": 10,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "UA",
                "requested": 3,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "PL",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "RO",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "US",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "DE",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "AU",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "CA",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "BR",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "IN",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "CN",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "JP",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "ZA",
                "requested": 1,
            },
            {
                "tags": {"include": [], "exclude": []},
                "type": "country",
                "value": "GB",
                "requested": 1,
            },
        ],
        "is_oneoff": True,
        "bill_to": bill_email,
    }


with open("targets.json") as targets_file:
    targets = json.load(targets_file)

print("Randomizing domains to measure to more effectively sample if credits run out")
domains_shuf = list(targets.keys())
random.shuffle(domains_shuf)

measurements = {}
skip_remaining = False

for domain in domains_shuf:
    backoff = 30
    time.sleep(backoff)
    if not skip_remaining:
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
                    print(
                        f"Request for {domain} measurement failed, no 'measurements' key in JSON response"
                    )
            else:
                print(
                    f"Request for {domain} measurement failed, response code was {request.status_code} instead of 201"
                )

            backoff = backoff * 2
            time.sleep(backoff)

            if backoff > 600:
                print(f"Failed to create measurement for {domain} too many times ...")
                print(
                    "This script probably exceeded a RIPE Atlas limit and is now stopping collection."
                )
                skip_remaining = True
                break

print("Waiting fifteen minutes to ensure (under normal conditions) all results load")
time.sleep(900)

probe_cache = {}
print("Beginning to fetch and enrich results ...")

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
                print(
                    f"Retrieved {len(response)} results from {domain} measurement {measurement}"
                )
                break
            else:
                print(f"Fail - response code was {request.status_code} instead of 200")

            backoff = backoff * 2
            time.sleep(backoff)

            if backoff > 60:
                print(f"Failed to retrieve results")
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
                    request = requests.get(
                        f"https://atlas.ripe.net/api/v2/probes/{result['prb_id']}/?format=json"
                    )
                    if request.status_code == 200:
                        response = request.json()
                        probe_cache[result["prb_id"]] = response
                        result["probe_data"] = response
                        print(
                            f"Retrieved probe data for probe {result['prb_id']} and cached result"
                        )
                        break
                    else:
                        print(
                            f"Fail - response code was {request.status_code} instead of 200"
                        )

                    backoff = backoff * 2
                    time.sleep(backoff)

                    if backoff > 15:
                        print(f"Failed to retrieve any probe data")
                        break

            updated_response.append(result)

        save_path = f"{args.output_folder}/{domain}/{measurement}/result.json"
        path = pathlib.Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        print(f"Saving enriched data to {save_path}")
        with open(save_path, "w") as result_file:
            json.dump(updated_response, result_file, indent=2)
