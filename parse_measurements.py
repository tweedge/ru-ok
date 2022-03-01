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
        "worldwide": {"successes": 0, "errors": 0, "sites_up": 0},
        "in Russia": {"successes": 0, "errors": 0, "sites_up": 0},
        "in Belarus": {"successes": 0, "errors": 0, "sites_up": 0},
    },
    "HTTPS (443)": {
        "worldwide": {"successes": 0, "errors": 0, "sites_up": 0},
        "in Russia": {"successes": 0, "errors": 0, "sites_up": 0},
        "in Belarus": {"successes": 0, "errors": 0, "sites_up": 0},
    },
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
        "worldwide": {"successes": 0, "errors": 0, "uptime_rate": 0},
        "in Russia": {"successes": 0, "errors": 0, "uptime_rate": 0},
        "in Belarus": {"successes": 0, "errors": 0, "uptime_rate": 0},
    }

    for result in results:
        if result["probe_data"]["country_code"] == "RU":
            cc = "in Russia"
        elif result["probe_data"]["country_code"] == "BY":
            cc = "in Belarus"
        elif result["probe_data"]["country_code"] == "UA":
            # not implemented yet
            continue
        elif result["probe_data"]["country_code"] == "PL":
            # not implemented yet
            continue
        elif result["probe_data"]["country_code"] == "RO":
            # not implemented yet
            continue
        else:
            cc = "worldwide"

        if m_type == "HTTPS (443)":
            if "err" in result.keys():
                bin = "errors"
            else:
                bin = "successes"
        elif m_type == "HTTP (80)":
            bin = "errors"
            for hop in result["result"]:
                if "error" in hop.keys():
                    continue
                else:
                    destination = result["dst_addr"]
                for packet in hop["result"]:
                    if "from" in packet.keys():
                        if packet["from"] == destination:
                            bin = "successes"
        else:
            print("not implemented, smartass")
            exit()

        summary[cc][bin] += 1
        totals[m_type][cc][bin] += 1

    for cc in ["in Russia", "in Belarus", "worldwide"]:
        measurement_count = 0
        for bin in ["successes", "errors"]:
            measurement_count += summary[cc][bin]

        try:
            uptime_rate = round((summary[cc]["successes"] / measurement_count) * 100)

            if uptime_rate > 70:
                totals[m_type][cc]["sites_up"] += 1
        except ZeroDivisionError:
            pprint(summary)
            exit()

        summary[cc]["uptime_rate"] = uptime_rate

    summaries.append(summary)

print("# All-Target Statistics")

domains_count = len(domains_in_sample.keys())
targets_count = len(targets.keys())
up = "sites_up"
for test in ["HTTP (80)", "HTTPS (443)"]:
    for cc in ["in Russia", "in Belarus", "worldwide"]:
        print(
            f"* **{totals[test][cc][up]}/{domains_count}** {test} sampled target sites up {cc}"
        )

print("")
print("Notes:")
print("* I am considering a site 'up' when it passes 70% or more uptime checks.")
print("* Not all targeted sites are guaranteed to be in in a given sample.")
print(f"* In this case, {domains_count}/{targets_count} targets sites were measured.")
print("")

for test in ["HTTP (80)", "HTTPS (443)"]:
    print(f"# Testing Individual Targets on {test}")
    print("| Sector | Domain | % Up WW | % Up RU | % Up BY | Remark |")
    print("|--------|--------|---------|---------|---------|--------|")

    table_contents = []
    for summary in summaries:
        if summary["type"] != test:
            continue

        pct_ww = summary["worldwide"]["uptime_rate"]
        pct_ru = summary["in Russia"]["uptime_rate"]
        pct_by = summary["in Belarus"]["uptime_rate"]

        if pct_ww + 40 < pct_ru or pct_ww + 40 < pct_by:
            quip = "**INTERESTING**"
        elif pct_ru + 40 < pct_ww or pct_by + 40 < pct_ww:
            quip = "**WEIRD**"
        else:
            quip = " "

        table_contents.append(
            f"| {targets[summary['domain']]['sector']} | `{summary['domain']}` | {pct_ww}% | {pct_ru}% | {pct_by}% | {quip} |"
        )

    table_contents.sort()
    for line in table_contents:
        print(line)

    if test == "HTTP (80)":
        print("")
        print(
            "*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via TCP (i.e. this is *not* application layer) to port 80 with an empty payload. This checks that the port is open and responsive, but not necessarily that the service itself is functioning. However, if the connection *failed* we should reasonably expect that the service is down as well - it is rare that sites do not run HTTP, even if only to redirect to HTTPS."
        )
        print("")
    elif test == "HTTPS (443)":
        print("")
        print(
            "*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via SSL/TLS (i.e. this is *not* application layer) to port 443 with the SNI set to the corresponding domain. This checks that the port is open and responsive *and* that a secure connection can be established, but not necessarily that the service itself is functioning. However, if the connection *failed* we may be able to expect that the service is down as well. Not all sites run HTTPS, but for those that were *previously* known to use HTTPS, this would reasonably indicate that those HTTPS services are down."
        )
        print("")
    else:
        print("")
        print(f"{test} is not implemented, smartass")
        print("")
