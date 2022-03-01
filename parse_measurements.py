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

all_results = []

for root, dirs, files in os.walk(args.input_folder):
    for file in files:
        with open(os.path.join(root, file), "r") as results_file:
            results = json.load(results_file)
            all_results.append(results)

summaries = []
domains_in_sample = {}
totals = {
    "HTTP (80)": {
        "worldwide": {
            "successes": 0,
            "errors": 0,
            "sites_up": 0
        },
       "in Russia": {
            "successes": 0,
            "errors": 0,
            "sites_up": 0
        }
    },
    "HTTPS (443)": {
        "worldwide": {
            "successes": 0,
            "errors": 0,
            "sites_up": 0
        },
       "in Russia": {
            "successes": 0,
            "errors": 0,
            "sites_up": 0
        }
    }
}

for results in all_results:
    domain = results[0]["dst_name"]
    if not domain in domains_in_sample.keys():
        domains_in_sample[domain] = True

    raw_m_type = results[0]["type"]
    if raw_m_type == "sslcert":
        m_type = "HTTPS (443)"
    elif raw_m_type == "traceroute":
        m_type = "HTTP (80)"
    else:
        print("not implemented, smartass")
        exit()

    summary = {
        "domain": domain,
        "type": m_type,
        "worldwide": {
            "successes": 0,
            "errors": 0,
            "uptime_rate": 0
        },
        "in Russia": {
            "successes": 0,
            "errors": 0,
            "uptime_rate": 0
        }
    }

    for result in results:
        if result["probe_data"]["country_code"] == "RU":
            cc = "in Russia"
        else:
            cc = "worldwide"

        if m_type == "HTTPS (443)":
            if "err" in result.keys():
                bin = "errors"
            else:
                bin = "successes"
        elif m_type == "HTTP (80)":
            bin = "successes"
            for hop in result["result"]:
                if "error" in hop.keys():
                    bin = "errors"
                elif hop["hop"] == 255:
                    bin = "errors"
        else:
            print("not implemented, smartass")
            exit()

        summary[cc][bin] += 1
        totals[m_type][cc][bin] += 1

    for cc in ["in Russia", "worldwide"]:
        measurement_count = 0
        for bin in ["successes", "errors"]:
            measurement_count += summary[cc][bin]

        uptime_rate = summary[cc]["successes"] / measurement_count
        summary[cc]["uptime_rate"] = uptime_rate

        if uptime_rate > 0.75:
            totals[m_type][cc]["sites_up"] += 1

    summaries.append(summary)

print("# All-Target Statistics")

domains = len(domains_in_sample.keys())
up = "sites_up"
for test in ["HTTP (80)", "HTTPS (443)"]:
    for cc in ["in Russia", "worldwide"]:
        print(f"* **{totals[test][cc][up]}/{domains}** {test} sampled target sites up {cc}")

print("")
print("Notes:")
print("* I am considering a site 'up' when it passes 75% or more uptime checks.")
print("* Not all targeted sites are guaranteed to be in in a given sample. Most are.")
print("")

for test in ["HTTP (80)", "HTTPS (443)"]:
    print(f"# Testing Individual Targets on {test}")
    print("| Remark | Domain | % Success WW | % Success RU |")
    print("| -------|--------|--------------|--------------|")

    for summary in summaries:
        if summary["type"] != test:
            continue

        quip = " "
        pct_ww = round(summary['worldwide']['uptime_rate'] * 100)
        pct_ru = round(summary['in Russia']['uptime_rate'] * 100)

        if pct_ww + 25 < pct_ru:
            quip = "**INTERESTING**"
        if pct_ru + 25 < pct_ww:
            quip = "**WEIRD**"
        print(
            f"| {quip} | `{summary['domain']}` | {pct_ww}% | {pct_ru}% |"
        )

    if test == "HTTP (80)":
        print("")
        print("*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via TCP (i.e. this is *not* application layer) to port 80 with an empty payload. This checks that the port is open and responsive, but not necessarily that the service itself is functioning. However, if the connection *failed* we should reasonably expect that the service is down as well - it is rare that sites do not run HTTP, even if only to redirect to HTTPS.")
        print("")
    elif test == "HTTPS (443)":
        print("")
        print("*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via SSL/TLS (i.e. this is *not* application layer) to port 443 with the SNI set to the corresponding domain. This checks that the port is open and responsive *and* that a secure connection can be established, but not necessarily that the service itself is functioning. However, if the connection *failed* we may be able to expect that the service is down as well. Not all sites run HTTPS, but for those that were *previously* known to use HTTPS, this would reasonably indicate that those HTTPS services are down.")
        print("")
    else:
        print("")
        print(f"{test} is not implemented, smartass")
        print("")
