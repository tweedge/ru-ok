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
total_successes_ww = 0
total_successes_ru = 0
total_errors_ww = 0
total_errors_ru = 0
total_sites_up_ww = 0
total_sites_up_ru = 0

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
                        total_errors_ru += 1
                    else:
                        errors_ww += 1
                        total_errors_ww += 1
                    if result["err"] in errors.keys():
                        errors[result["err"]] += 1
                    else:
                        errors[result["err"]] = 1
                else:
                    if result["probe_data"]["country_code"] == "RU":
                        successes_ru += 1
                        total_successes_ru += 1
                    else:
                        successes_ww += 1
                        total_successes_ww += 1

            total_checks_ww = successes_ww + errors_ww
            uptime_rate_ww = successes_ww / total_checks_ww
            total_checks_ru = successes_ru + errors_ru
            uptime_rate_ru = successes_ru / total_checks_ru

            if uptime_rate_ww > 0.75:
                total_sites_up_ww += 1
            if uptime_rate_ru > 0.75:
                total_sites_up_ru += 1

            summary = {
                "successes_ww": successes_ww,
                "successes_ru": successes_ru,
                "errors_ww": errors_ww,
                "errors_ru": errors_ru,
                "uptime_rate_ww": uptime_rate_ww,
                "uptime_rate_ru": uptime_rate_ru,
                "errors": errors
            }
            summaries[domain] = summary

print("# All-Target Statistics")
print(f"* {total_sites_up_ww}/{len(targets.keys())} sites up worldwide ({total_successes_ww}/{(total_successes_ww+total_errors_ww)} checks passed)")
print(f"* {total_sites_up_ru}/{len(targets.keys())} sites up in Russia ({total_successes_ru}/{(total_successes_ru+total_errors_ru)} checks passed)")
print("")
print("Note: I am considering a site 'up' when it passes 75% or more uptime checks")
print("")
print("# Specific Targets")

for domain, summary in summaries.items():
    percent_up_ww = round(summary["uptime_rate_ww"] * 100)
    percent_up_ru = round(summary["uptime_rate_ru"] * 100)
    print(f"* `{domain}` passed {percent_up_ww}% of checks globally, vs {percent_up_ru}% in Russia")