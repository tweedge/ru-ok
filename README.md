# ru-ok "Are you (RU) ok?"

**Note: While this repository discusses the results of hacktivism in the Russo-Ukrainian War, I am not personally participating in that hacktivism, and I am not condoning or encouraging hacktivism in this repository. For people looking to help Ukraine, especially nontechnical people who have been using certain webpages to "DDoS" Russia, please look into safe and legal options [listed here](https://www.npr.org/2022/02/25/1082992947/ukraine-support-help).**

This is a very quick project to assess the status of Russian internet properties (via RIPE Atlas) being targeted by hacktivists. Specifically, I am evaluating every target listed in Ukraine's hacktivist "IT ARMY" Telegram group with 100 unique probes (50 worldwide, and 50 *within Russia*) to check for service availability on both HTTP and HTTPS.

I wanted to check connectivity from within Russia's borders because I saw many mixed reports across Twitter and Reddit, with international parties (Americans, Ukrainians, etc.) claiming many sites had been knocked offline, where Russians chimed in that many sites remained online for them. Given that Russia has a sovereign internet policy and can do as much as [disconnect themselves from the internet entirely](https://www.reuters.com/technology/russia-disconnected-global-internet-tests-rbc-daily-2021-07-22/) - could Russia be dropping most/all traffic at the edge of the country (ex. using their transit providers) before the DDoS traffic hit the targets?

Based on the measurements I took, I was partially correct - per the last run around 2022-02-28 ~03:00:00 UTC, the status of all targets is:
* **42/92** HTTP (80) targeted sites up in Russia
* **20/92** HTTP (80) targeted sites up worldwide
* **38/92** HTTPS (443) targeted sites up in Russia
* **28/92** HTTPS (443) targeted sites up worldwide

So there is measurably higher availability for several target sites within Russia's borders, but unless traffic from known RIPE Atlas probes is also filtered (unlikely), Russia is still facing substantial outages in the face of hacktivism.

The most recent uptime statistics for each site are also available in [STATUS.md](https://github.com/tweedge/ru-ok/blob/main/STATUS.md), and you can use this to see which sites have the most interesting availability characteristics at-a-glance. For example, the Kremlin site has been quoted as offline by many people on Reddit and Twitter. As of the last scan, we can clearly see that while `kremlin.ru` has <20% availability internationally, it has ~80% availability within Russia - a stark difference.

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

## Methodology

To get a better sense of the global situation, I elected to use [RIPE Atlas](https://atlas.ripe.net/) to run some active measurements against each domain targeted by the IT ARMY of Ukraine Telegram.

Why RIPE Atlas? Atlas is a project by [RIPE NCC](https://www.ripe.net/) is a global network of probes that measure Internet connectivity and reachability, providing a deep understanding of the state of the Internet. Probes are hosted by ordinary people on their regular home or business network - I am a probe host, as are my parents - and can be used by contributors to run a handful of connectivity tests (ex. ping, traceroute, DNS lookups) against any internet-accessible host. Very importantly, this gives us a view of the internet from the probe's connection without using a VPN (unless the entire network the probe is on is being tunneled through one, which is generally unlikely).

For each measurement:
* I input a target domain
* I request 25 probes from anywhere in the world, and another 25 probes from only within Russian IP space
* All probes individually perform a DNS lookup for the target domain
* If the DNS lookup is successful, all probes perform their desired measurement check (more on this in a minute)
* Probes report the data retrieved - or any errors encountered - to RIPE Atlas
* I collect the measurement information after waiting 15 minutes and analysis on it

Afterwards, results are uploaded to this GitHub. Due to the daily cap on results I can collect, I will try to run this analysis every few hours, but cannot run this continually without breaching my account quotas.

### Measurements Taken

The caveat to this approach is that, while we have access to reliable connectivity data from within Russia itself, the measurements themselves are not application-layer. RIPE Atlas is designed for network operators and only supports common network protocols - it explicitly and intentionally does *not* support application-layer checks.

**For HTTP**: The measurement connects via TCP (i.e. this is *not* application layer) to port 80 with an empty payload. This checks that the port is open and responsive, but not necessarily that the service itself is functioning. However, if the connection *failed* we should reasonably expect that the service is down as well - it is rare that sites do not run HTTP, even if only to redirect to HTTPS.

**For HTTPS**: The measurement connects via SSL/TLS to port 443 with the SNI set to the corresponding domain. This checks that the port is open and responsive *and* that a secure connection can be established, but not necessarily that the service itself is functioning. However, if the connection *failed* we may be able to expect that the service is down as well. Not all sites run HTTPS, but for those that were *previously* known to use HTTPS, this would reasonably indicate that those HTTPS services are down.

## FAQ

#### How can I help you measure this stuff?

If you have RIPE Atlas credits, run your own analysis, do new studies, fork this hacked-together code, have fun with it!

If you have spare RIPE Atlas credits that you don't want/need, I'd certainly appreciate any credit donation you can spare! Reach out to me on [Twitter](https://twitter.com/_tweedge) or [Reddit](https://www.reddit.com/user/tweedge) if that's the case and I'll send you my RIPE Atlas email.

#### Why did you make a snide comment about websites that "DDoS" people earlier?

They're low throughput compared to any real DDoS tool, they're especially easy to neuter (site operators can disable all [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) requests by denying the HTTP OPTIONS method), several are made anonymously (and who knows if your IP/information is being logged straight to the Kremlin), etc. It's not a good way to get involved.

#### How can I get involved?

Read over the resources [here](https://www.npr.org/2022/02/25/1082992947/ukraine-support-help). Spread factual information about the invasion - even take the time to fact-check yourself before you post. Accept that many Russians do not want this. Practice compassion. There are thousands of soldiers dying on both sides at a politicians' whim again.

#### I meant how can I get involved in *hacktivism*.

I'm not going to tell you that and I'm explicitly not encouraging it.

#### How are you connecting to a specific TCP port using RIPE Atlas?

It's a "TCP Ping" - using traceroute with TCP instead of the usual ICMP. You can see this workaround described by Vesna Manojlovic in [Measuring Reachability of your Web Server using RIPE Atlas](https://www.ripe.net/support/training/ripe-ncc-educa/presentations/measuring-reachability-of-your-web-server-using-ripe-atlas.pdf) - it's a neat trick.