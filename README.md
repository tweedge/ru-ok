# ru-ok "Are you (RU) ok?"

**Note: While this repository discusses the results of hacktivism in the Russo-Ukrainian War, I am not personally participating in that hacktivism, and I am not condoning or encouraging hacktivism in this repository. For people looking to help Ukraine, especially nontechnical people who have been using certain webpages to "DDoS" Russia, please look into safe and legal options [listed here](https://www.npr.org/2022/02/25/1082992947/ukraine-support-help).**

This is a very quick project to assess the status of Russian internet properties (via RIPE Atlas) being targeted by hacktivists. Specifically, I am evaluating every target listed in Ukraine's hacktivist "IT ARMY" Telegram group with 50 unique probes (25 worldwide, and 25 *within Russia*) to check for service availability.

I wanted to check connectivity from within Russia's borders because I saw many mixed reports across Twitter and Reddit, with international parties (Americans, Ukrainians, etc.) claiming many sites had been knocked offline, where Russians chimed in that many sites remained online for them. Given that Russia has a sovereign internet policy and can do as much as [disconnect themselves from the internet entirely](https://www.reuters.com/technology/russia-disconnected-global-internet-tests-rbc-daily-2021-07-22/) - could Russia simply be dropping DDoS traffic at the edge of the country (ex. using their transit providers) before the traffic hit the targets?

Based on the measurements I took, I was partially correct - per the last run around 2022-02-27 ~19:15:00 UTC, the status of all targets is:
* **28/92** sites up worldwide (733/2205 checks passed)
* **41/92** sites up in Russia (1033/2252 checks passed)

So there is measurably higher availability for several target sites within Russia's borders, but unless traffic from known RIPE Atlas probes is also filtered (unlikely), Russia is still facing substantial outages in the face of hacktivism. For those curious, the most recent uptime statistics for each site are also available in [STATUS.md](https://github.com/tweedge/ru-ok/blob/main/STATUS.md).

## Why?

This is a phenomenally interesting time to be working in cybersecurity - we are seeing hacktivism sanctioned and employed directly in international conflicts for the first time. All cybersecurity professionals should be paying attention to this, and I want to find out as much as possible about the *results* of Ukraine's committment to hacktivism during this conflict.

## Problems with Existing Measurements

Beyond the conflicting reports that I covered earlier - usually from anonymous people on the internet, so who knows how reliable their claims are or how they're connected to the world - there are problems even in "official" reporting. Ukraine itself has been claiming that all or almost all targets were offline via the IT ARMY of Ukraine Telegram channel, and their screenshot tipped me off to a problem: I'd used the uptime-checking service they were using before.

The uptime checker seen in [this screenshot](https://t.me/itarmyofukraine2022/44) is *almost certainly* Uptime Robot, which I monitored my sites with for years. Uptime Robot uses a primary site in Dallas, Texas, USA for their uptime checks, and also uses international monitors to confirm downtime before a notification is sent. The locations they administrate - and the IPs for all of them - are available [on this page](https://uptimerobot.com/help/locations/). Importantly, none of these are in Russia.

Ukraine's Telegram group administrators also used a couple [other sites](https://t.me/itarmyofukraine2022/33) to display downtime and rally followers with the same issue: no RU presence.

So, how can we get a higher-accuracy assessment of the situation without:
* Just trusting internet strangers
* Trying to use a VPN to 'appear' in Russia (which undoubtedly many others are doing right now, and may be rate-limited or blocked)
* Physically being in Russia

### Methodology

To get a better sense of the global situation, I elected to use [RIPE Atlas](https://atlas.ripe.net/) to run some active measurements against each domain targeted by the IT ARMY of Ukraine Telegram.

Why RIPE Atlas? Atlas is a project by [RIPE NCC](https://www.ripe.net/) is a global network of probes that measure Internet connectivity and reachability, providing a deep understanding of the state of the Internet. Probes are hosted by ordinary people on their regular home or business network - I am a probe host, as are my parents - and can be used by contributors to run a handful of connectivity tests (ex. ping, traceroute, DNS lookups) against any internet-accessible host. Very importantly, this gives us a view of the internet from the probe's connection without using a VPN (unless the entire network the probe is on is being tunneled through one, which is generally unlikely).

For each measurement:
* I input a target domain
* I request 25 probes from anywhere in the world, and another 25 probes from only within Russian IP space
* All probes individually perform a DNS lookup for the target domain
* If the DNS lookup is successful, all probes individually to make an SSL/TLS connection on port 443
* Probes report the certificate retrieved - or any errors encountered - to RIPE Atlas
* I collect the measurement information after waiting 15 minutes and analysis on it

Afterwards, results are uploaded to this GitHub. Due to the daily cap on results I can collect, I will try to run this analysis every few hours, but cannot run this continually without breaching my account quotas.