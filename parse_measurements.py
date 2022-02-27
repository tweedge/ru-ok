import argparse
import json
import os
from pprint import pprint

parser = argparse.ArgumentParser(
    description="Assess enriched measurements from RIPE ATLAS of SSL connectivity to targets"
)
parser.add_argument(
    "--input-folder",
    action="store",
    type=str,
    required=True,
    help="Input folder relative to current working directory of all results",
)
args = parser.parse_args()

with open("targets.json") as targets_file:
    targets = json.load(targets_file)

summaries = {}
for root, dirs, files in os.walk(args.input_folder):
    for file in files:
        with open(os.path.join(root, file), "r") as results_file:
            results = json.load(results_file)
            domain = results[0]["dst_name"]
            
            successes_ww = 0
            successes_ru = 0
            errors_ww = 0
            errors_ru = 0
            errors = {}
            for result in results:
                if "err" in result.keys():
                    if result["probe_data"]["country_code"] == "RU":
                        errors_ru += 1
                    else:
                        errors_ww += 1
                    if result["err"] in errors.keys():
                        errors[result["err"]] += 1
                    else:
                        errors[result["err"]] = 1
                else:
                    if result["probe_data"]["country_code"] == "RU":
                        successes_ru += 1
                    else:
                        successes_ww += 1

            summary = {
                "successes_ww": successes_ww,
                "successes_ru": successes_ru,
                "errors_ww": errors_ww,
                "errors_ru": errors_ru,
                "errors": errors
            }
            summaries[domain] = summary

for domain, summary in summaries.items():
    total_checks_ww = summary["successes_ww"] + summary["errors_ww"]
    uptime_rate_ww = summary["successes_ww"] / total_checks_ww
    total_checks_ru = summary["successes_ru"] + summary["errors_ru"]
    uptime_rate_ru = summary["successes_ru"] / total_checks_ru

    print(f"### `{domain}`")
    print(f"* {summary['successes_ww']}/{total_checks_ww} SSL checks passed worlwide")
    print(f"* {summary['successes_ru']}/{total_checks_ru} SSL checks passed in Russia")
    print("")