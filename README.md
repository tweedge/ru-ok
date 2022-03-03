# ru-ok "Are you (RU) ok?"

**Note: While this repository discusses the results of hacktivism in the Russo-Ukrainian War, I am not personally participating in that hacktivism, and I am not condoning or encouraging hacktivism in this repository. For people looking to help Ukraine, especially nontechnical people who have been using certain webpages to "DDoS" Russia, please look into safe and legal options [listed here](https://www.npr.org/2022/02/25/1082992947/ukraine-support-help).**

This is a very quick project to assess the status of Russian internet properties (via RIPE Atlas) being targeted by hacktivists. Specifically, I am evaluating every target listed in Ukraine's hacktivist "IT ARMY" Telegram group with many unique probes to check for service availability on both HTTP and HTTPS.

I wanted to check connectivity from within Russia's borders because I saw many mixed reports across Twitter and Reddit, with international parties (Americans, Ukrainians, etc.) claiming many sites had been knocked offline, where Russians chimed in that many sites remained online for them. The truth is more complex - availability for Russians is being prioritized by many RU-local sites, and international traffic may be facing extreme congestion, or simply be sinkholed in some cases.

Per the last run around 2022-03-03 ~04:00:00 UTC, the status of sampled targets is:
* **85/175** HTTP (80) sampled target sites up in Russia
* **102/175** HTTP (80) sampled target sites up in Belarus
* **24/175** HTTP (80) sampled target sites up worldwide
* **95/175** HTTPS (443) sampled target sites up in Russia
* **109/175** HTTPS (443) sampled target sites up in Belarus
* **70/175** HTTPS (443) sampled target sites up worldwide

So there is measurably higher availability for several target sites within Russia's borders, but unless traffic from known RIPE Atlas probes is also filtered (unlikely), Russia is still facing substantial outages in the face of hacktivism.

The most recent uptime statistics for each site (binned by sector) are also available in [STATUS.md](https://github.com/tweedge/ru-ok/blob/main/STATUS.md), and you can use this to see which sites have the most interesting availability characteristics at-a-glance. For example, the Kremlin site has been quoted as offline by many people on Reddit and Twitter. From my scanning, we can clearly see that while `kremlin.ru` often appears 'down' internationally, it has near-normal (80%+) availability within Russia - a stark difference.

## Why?

This is a phenomenally interesting time to be working in cybersecurity - we are seeing hacktivism sanctioned and employed directly in international conflicts for the first time. All cybersecurity professionals should be paying attention to this, and I want to find out as much as possible about the *results* of Ukraine's committment to hacktivism during this conflict.

## Problems with Existing Measurements

Beyond the conflicting reports that I covered earlier - usually from anonymous people on the internet, so who knows how reliable their claims are or how they're connected to the world - there are problems even in "official" reporting. Ukraine itself has been claiming that all or almost all targets were offline via the IT ARMY of Ukraine Telegram channel, and their screenshot tipped me off to a problem: I'd used the uptime-checking service they were using before.

The uptime checker seen in [this screenshot](https://t.me/itarmyofukraine2022/44) is *almost certainly* Uptime Robot, which I monitored my sites with for years. Uptime Robot uses a primary site in Dallas, Texas, USA for their uptime checks, and also uses international monitors to confirm downtime before a notification is sent. The locations they administrate - and the IPs for all of them - are available [on this page](https://uptimerobot.com/help/locations/). Importantly, none of these are in Russia.

Ukraine's Telegram group administrators also used a couple [other sites](https://t.me/itarmyofukraine2022/33) to display downtime and rally followers with the same issue: no RU presence.

So, how can we get a higher-accuracy assessment of the situation without:
* Just trusting internet strangers
* Trying to use a VPN to 'appear' in Russia/Belarus (which undoubtedly many others are doing right now, and may be rate-limited or blocked)
* Physically being in Russia/Belarus

## Methodology

To get a better sense of the global situation, I elected to use [RIPE Atlas](https://atlas.ripe.net/) to run some active measurements against each domain targeted by the IT ARMY of Ukraine Telegram.

Why RIPE Atlas? Atlas is a project by [RIPE NCC](https://www.ripe.net/) is a global network of probes that measure Internet connectivity and reachability, providing a deep understanding of the state of the Internet. Probes are hosted by ordinary people on their regular home or business network - I am a probe host, as are my parents - and can be used by contributors to run a handful of connectivity tests (ex. ping, traceroute, DNS lookups) against any internet-accessible host. Very importantly, this gives us a view of the internet from the probe's connection without using a VPN (unless the entire network the probe is on is being tunneled through one, which is generally unlikely).

For each measurement:
* I input a target domain or IP
* I request 10 probes from a sample major internet-connected countries worldwide, plus 10 probes from only within Russian IP space, plus 10 *more* probes from only within Belarusian IP space
  * **New:** I'm also collecting 3 measurements from Ukraine, 1 from Poland, and 1 from Romainia. Not doing anything with them yet though - stay tuned!
* If required, all probes individually perform a DNS lookup for the target domain
* All probes perform their desired measurement check (more on this in a minute)
* Probes report the data retrieved - or any errors encountered - to RIPE Atlas
* I collect the measurement information after waiting a minimum of 15 minutes and run analysis on it

Afterwards, results are uploaded to this GitHub. Due to the daily cap on results I can collect, I will try to run this analysis every ~12 hours, but cannot run this continually without breaching my account quotas.

**New:** Due to an ever-increasing number of targets listed by "IT ARMY of Ukraine" this repository will now randomly sample targets, grabbing partial results if/when I run out of credits.

### Measurements Taken

The caveat to this approach is that, while we have access to reliable connectivity data from within Russia itself, the measurements themselves are not application-layer. RIPE Atlas is designed for network operators and only supports common network protocols - it explicitly and intentionally does *not* support application-layer checks.

**For HTTP**: The measurement connects via TCP (i.e. this is *not* application layer) to port 80 with an empty payload. This checks that the port is open and responsive, but not necessarily that the service itself is functioning. However, if the connection *failed* we should reasonably expect that the service is down as well - it is rare that sites do not run HTTP, even if only to redirect to HTTPS.

**For HTTPS**: The measurement connects via SSL/TLS to port 443 with the SNI set to the corresponding domain. This checks that the port is open and responsive *and* that a secure connection can be established, but not necessarily that the service itself is functioning. However, if the connection *failed* we may be able to expect that the service is down as well. Not all sites run HTTPS, but for those that were *previously* known to use HTTPS, this would reasonably indicate that those HTTPS services are down.

### Caveats

**No direct DNS server testing.** On 2022-02-28, IT ARMY instructed readers to DDoS DNS servers belonging to `www.sberbank.ru`:

* 194.54.14.186
* 194.54.14.187
* 194.67.7.1
* 194.67.2.109

I cannot measure the impact to these servers, as I haven't found a way to reliably do UDP port checking with RIPE Atlas (for a transport-level check), and the DNS resolution measurement is resolving a domain name with the *probe's* resolver (you cannot input a custom resolver to test).

*If* these are the authoritative servers for `www.sberbank.ru` - I don't know/haven't checked - then that would be caught in any existing measurement with a DNS failure. Further, a success doesn't necessarily mean the targeted DNS servers would be up or down *anyway* (due to resolver caching). So in my opinion, this is not worth pursuing.

**No testing internationalized domain names.** On 2022-03-01, IT ARMY instructed readers to take down `объясняем.рф`. Attempting to start RIPE Atlas measurements against this domain, the requests failed with a status code of 400. I am triaging this for later results and hope to add this to the sample, for examply by punycoding the domain before attempting to start the sample.

## FAQ

#### How can I help you measure this stuff?

If you have RIPE Atlas credits, run your own analysis, do new studies, fork this hacked-together code, have fun with it!

If you have spare RIPE Atlas credits that you don't want/need, I'd certainly appreciate any credit donation you can spare! Reach out to me on [Twitter](https://twitter.com/_tweedge) or [Reddit](https://www.reddit.com/user/tweedge) if that's the case and I'll send you my RIPE Atlas email.

#### How can I get involved in other ways?

Read over the resources [here](https://www.npr.org/2022/02/25/1082992947/ukraine-support-help). Spread factual information about the invasion - even take the time to fact-check yourself before you post. Accept that many Russians do not want this. Practice compassion. There are thousands of soldiers dying on both sides at a politicians' whim again.

#### I meant how can I get involved in *hacktivism*.

I'm not going to tell you that.

#### Why did you make a snide comment about websites that "DDoS" people earlier?

They're low throughput compared to any real DDoS tool, they're especially easy to neuter (site operators can disable all [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) requests by denying the HTTP OPTIONS method, and you shouldn't disable CORS in your browser to bypass this...), several are made anonymously (and who knows if your IP/information is being logged straight to the Kremlin), etc. It's not a good way to get involved.

#### How are you connecting to a specific TCP port using RIPE Atlas?

It's a "TCP Ping" - using traceroute with TCP instead of the usual ICMP. You can see this workaround described by Vesna Manojlovic in [Measuring Reachability of your Web Server using RIPE Atlas](https://www.ripe.net/support/training/ripe-ncc-educa/presentations/measuring-reachability-of-your-web-server-using-ripe-atlas.pdf) - it's a neat trick.
