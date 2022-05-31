# RU-OK? ("Are you - RU - ok?")

**Note: While this repository discusses the results of hacktivism in the Russo-Ukrainian War, I am not personally participating in that hacktivism, and I am not condoning or encouraging hacktivism in this repository. For people looking to help Ukraine, especially nontechnical people who have been using certain webpages to "DDoS" Russia, please look into safe and legal options [listed here](https://www.npr.org/2022/02/25/1082992947/ukraine-support-help).**

**Important Update: RU-OK? is not currently collecting new measurements. Please see "Soft Stop" under the Methodology section for more details.**

This is a very quick project to assess the status of Russian internet properties (via RIPE Atlas) being targeted by hacktivists. Specifically, I evaluated almost every target listed in Ukraine's hacktivist "IT ARMY" Telegram group with many unique probes between `2022-02-27` and `2022-05-30` to check for service availability.

I wanted to check connectivity from within Russia's borders because I saw many mixed reports across Twitter and Reddit, with international parties (Americans, Ukrainians, etc.) claiming many sites had been knocked offline, where Russians chimed in that many sites remained online for them. The truth is more complex - availability for Russians is being prioritized by many RU-local sites, and international traffic may be facing extreme congestion, or simply be sinkholed in some cases.

The uptime statistics as of `2022-05-30` for each site are also available in the final [STATUS.md](https://github.com/tweedge/ru-ok/blob/main/STATUS.md), and while this project was collecting new measurements you could use this to see which sites have the most interesting availability characteristics daily at-a-glance. You can also use the commit history to look through prior days' summaries. There is measurably higher availability for several target sites within Russia's borders, but unless traffic from known RIPE Atlas probes is also filtered (unlikely), Russia is still facing substantial outages in the face of hacktivism. For example, the Kremlin site has been quoted as offline by many people on Reddit and Twitter. From my scanning, we can clearly see that while `kremlin.ru` may appear 'down' internationally, it has near-normal (80%+) availability within Russia - a stark difference.

## Why?

This is a phenomenally interesting time to be working in cybersecurity - we are seeing hacktivism sanctioned and employed directly in international conflicts for the first time. All cybersecurity professionals should be paying attention to this - while "cyberwar" is not the forefront of conflict in the sense that it's costing lives on either side of the battlefield, the disruptions and defender-chaos that Ukraine has caused through its rallying is going to be a blueprint for hacktivism's role in future global conflicts. I want to find out as much as possible about the *results* of Ukraine's committment to hacktivism during this conflict, as this is the only time that data such as this can be collected - while it happens.

**Edit** - I'm not the only one interested in Ukraine's impact, and these results (or my analysis of them) have been cited in the following articles, among others:

* Ukraine’s IT army is doing well, hitting Russia with ‘cost and chaos’ - [VentureBeat](https://venturebeat.com/2022/03/04/ukraines-it-army-is-doing-well-hitting-russia-with-cost-and-chaos/)
* Ukraine deserves an IT army. We have to live with the fallout - [VentureBeat](https://venturebeat.com/2022/03/04/ukraine-deserves-an-it-army-we-have-to-live-with-the-fallout/)
* Ukraine: We’ve repelled ‘nonstop’ DDoS attacks from Russia - [VentureBeat](https://venturebeat.com/2022/03/07/ukraine-weve-repelled-nonstop-ddos-attacks-from-russia/)
* Guerre en Ukraine : les cyberattaques contre la Russie, le « cri de colère » d’une armée de volontaires - [Le Monde](https://www.lemonde.fr/pixels/article/2022/03/25/guerre-en-ukraine-face-a-la-russie-les-cyberattaques-en-forme-de-cri-de-colere-d-une-armee-de-volontaires_6119064_4408996.html)
* Ukraine Demanded Cloudflare Stop Protecting Russians From Cyberattacks. Cloudflare Said No - [Forbes](https://www.forbes.com/sites/thomasbrewster/2022/03/07/cloudflare-rejects-ukraines-call-to-stop-protecting-russians-from-cyberattacks/)

I am available via Twitter, Keybase, etc. to discuss or provide analysis where I can, and am comfortable going on the record about areas I am a subject matter expert in. For example, I generally won't comment on what Ukrainian/Russian sites are being *breached* as that isn't what this project measures - only the results of DDoS-centric hacktivism that Ukraine has cultivated.

## Problems with Existing Measurements

Beyond the conflicting reports that I covered earlier - usually from anonymous people on the internet, so who knows how reliable their claims are or how they're connected to the world - there are problems even in "official" reporting. Ukraine itself has been claiming that all or almost all targets were offline via the IT ARMY of Ukraine Telegram channel, and their screenshot tipped me off to a problem: I'd used the uptime-checking service they were using before.

The uptime checker seen in [this screenshot](https://t.me/itarmyofukraine2022/44) is *almost certainly* Uptime Robot, which I monitored my sites with for years. Uptime Robot uses a primary site in Dallas, Texas, USA for their uptime checks, and also uses international monitors to confirm downtime before a notification is sent. The locations they administrate - and the IPs for all of them - are available [on this page](https://uptimerobot.com/help/locations/). Importantly, none of these are in Russia.

Ukraine's Telegram group administrators also used a couple [other sites](https://t.me/itarmyofukraine2022/33) to display downtime and rally followers with the same issue: no RU presence.

So, how can we get a higher-accuracy assessment of the situation without:
* Just trusting internet strangers
* Trying to use a VPN to 'appear' in Russia/Belarus (which undoubtedly many others are doing right now, and may be rate-limited or blocked)
* Physically being in Russia/Belarus

## Methodology

To get a better sense of the global situation, I elected to use [RIPE Atlas](https://atlas.ripe.net/) to run some active measurements against each domain or IP targeted by the IT ARMY of Ukraine Telegram, and did so from `2022-02-27` to `2022-05-30`.

Why RIPE Atlas? Atlas is a project by [RIPE NCC](https://www.ripe.net/) is a global network of probes that measure Internet connectivity and reachability, providing a deep understanding of the state of the Internet. Probes are hosted by ordinary people on their regular home or business network - I am a probe host, as are my parents - and can be used by contributors to run a handful of connectivity tests (ex. ping, traceroute, DNS lookups) against any internet-accessible host. Very importantly, this gives us a view of the internet from the probe's connection without using a VPN (unless the entire network the probe is on is being tunneled through one, which is generally unlikely).

For each measurement:
* I input a target domain or IP
* I request 10 probes from a sample major internet-connected countries worldwide, plus 10 probes from only within Russian IP space, plus 5 *more* probes from only within Belarusian IP space (for SSL measurements)
  * **New:** I'm also collecting 3 measurements from Ukraine, 1 from Poland, and 1 from Romainia. Not doing anything with them yet though - stay tuned!
  * **Changed:** Due to the number of targets and relatively low number of Belarusian targets, the sampling rate for Belarus has decreased to 5 probes per measurement from 10.
  * **Changed:** Due to the high cost of TCP "ping" measurements in the RIPE Atlas system (these are actually TCP-based traceroutes, see FAQ), the results collected are going to be halved starting on 2022-03-17.
* If required, all probes individually perform a DNS lookup for the target domain
* All probes perform their desired measurement check (more on this in a minute)
* Probes report the data retrieved - or any errors encountered - to RIPE Atlas
* I collect the measurement information after waiting a minimum of 15 minutes and run analysis on it

Afterwards, results are uploaded to this GitHub. **Edit:** I will be running this analysis every *24 hours* starting March 8th instead of every 12 hours. Due to an ever-increasing number of targets listed by "IT ARMY of Ukraine" this repository will now randomly sample targets, grabbing partial results if/when I run out of credits.

### Measurements Taken

The caveat to this approach is that, while we have access to reliable connectivity data from within Russia itself, the measurements themselves are not application-layer. RIPE Atlas is designed for network operators and only supports common network protocols - it explicitly and intentionally does *not* support application-layer checks.

**For HTTP**: The measurement connects via TCP (i.e. this is *not* application layer) to port 80 with an empty payload. **This checks that the port is open and responsive, but not necessarily that the service itself is functioning.** However, if the connection *failed* we should reasonably expect that the service is down as well - it is rare that sites do not run HTTP, even if only to redirect to HTTPS.

**For HTTPS**: The measurement connects via SSL/TLS to port 443 with the SNI set to the corresponding domain. **This checks that the port is open and responsive *and* that a secure connection can be established, but not necessarily that the service itself is functioning.** However, if the connection *failed* we may be able to expect that the service is down as well. Not all sites run HTTPS, but for those that were *previously* known to use HTTPS, this would reasonably indicate that those HTTPS services are down.

**For unusual TCP ports**: The measurement connects via TCP to the specified port with an empty payload. **This *usually* works to check that the port is open and responsive, but requires further analysis before I add this data to summaries.** Currently, the data is collected but not reported on in the README or STATUS documents.

TL;DR: if the connection checks (especially HTTP/HTTPS) are failing, a tested entity is confidently down *at the time this project checked, from the probes used to test with*. However, it is possible for sites to be marked "up" if the *website's network layer* is functioning, but the *website's application* is not (ex. if connecting to a CDN, the CDN may be up, even if the website's backend is overloaded and offline).

### Gaps

**No direct DNS server testing.** On 2022-02-28, IT ARMY instructed readers to DDoS DNS servers belonging to `www.sberbank.ru` - `194.54.14.186`, `194.54.14.187`, `194.67.7.1`, and `194.67.2.109`.

I cannot measure the impact to these servers, as I haven't found a way to reliably do UDP port checking with RIPE Atlas (for a transport-level check), and the DNS resolution measurement is resolving a domain name with the *probe's* resolver (you cannot input a custom resolver to test).

*If* these are the authoritative servers for `www.sberbank.ru` - I don't know/haven't checked - then that would be caught in any existing measurement with a DNS failure. Further, a success doesn't necessarily mean the targeted DNS servers would be up or down *anyway* (due to resolver caching). So in my opinion, this is not worth pursuing.

Again on 2022-03-08, IT ARMY instructed readers to DDoS DNS servers, this time belonging to the Russian Railway. These were `217.175.155.100`, `217.175.155.12`, and `217.175.140.71`.

And again on 2022-03-13, IT ARMY instructed readers to DDoS `92.53.97.198` (which this project cannot measure) as part of the attacks on `alfabank.ru`.

...and so on. This keeps occasionally happening, and is no longer a unique enough event to note. TL;DR it's a known gap.

**No UDP testing.** Same problem as above, new port. On 2022-03-09, IT ARMY listed UDP 500 as open on IP `77.247.242.173` (belonging to `nspk.ru`) - UDP reachability cannot be reliably assessed using RIPE Atlas to my knowledge.

**No testing internationalized domain names.** On 2022-03-01, IT ARMY instructed readers to take down `объясняем.рф`. Attempting to start RIPE Atlas measurements against this domain, the requests failed with a status code of 400. As IDNs are not a significant minority of targets, I'm electing to skip these. The same goes for `пиломатериалы.рф`, which IT ARMY targeted starting on 2022-03-29.

**No testing where existing service ports aren't known.** On 2022-03-04, IT ARMY's only new targets were NSPK public IPs (serving "Myr" bank cards), which do not have known open ports via Shodan or Censys, either due to a request from NSPK, or blocking their scanners, etc. Given no ports are known, I cannot assess uptime accurately with RIPE Atlas' tooling.

**No immediate testing**: On 2022-03-05, IT ARMY intelligently weaponized their audience to take down a fake website, `savelife.pw` (by reporting it to the registrar, hosting companies, etc.). The scans I am running are long-term, meant to understand the cyber-conflict broadly, and not ongoing or immediate assessments of sites. Before I could add this to uptime checks, the site was taken down.

**TCP results for non-port-80 pings prior to 2022-03-17 are invalid**: This was due to a (dumb, preventable) bug in my code, and I apologize. All webserver tests, which are summarized in this README and in STATUS.md, are however 100% valid. I wasn't doing anything with the TCP data and therefore didn't notice the inconsistent results which pointed to a bug.

### Soft Stop

**As of 2022-05-30, I have stopped collecting new measurements.** The reasons for this are principally:

1. The current dataset answered questions about the development and effectiveness of Ukraine's hacktivist offensive, which was its stated original goal.
2. The current dataset may also answer some questions about a. the impact of reduced international focus on Ukraine's DDoS-centric hacktivism (both via media cycles moving on, and to more sophisticated hacktivism leading to data breaches, etc.) or b. the reduced impact of DDoS attacks via increased Russian fortification of key websites in the past few months. However, *additional* data collection with this same methodology is unlikely to help better-answer these questions.

This project will restart if these are more questions that data like this can help answer. I am keeping an eye on IT ARMY Telegram, as well as the various predictions of increased/decreased conflict come September, where new data could be valuable. While there aren't new answers I can bring to light currently, the bloody conflict in Ukraine continues, and I again encourage anyone in a position to help to please look into safe and legal options [listed here](https://www.npr.org/2022/02/25/1082992947/ukraine-support-help).

I am extremely thankful to the people I met along the way who helped with this project, provided feedback and support, and offered to donate RIPE Atlas credits to sustain these measurements. In particular, thank you to [Bob Rudis](https://twitter.com/hrbrmstr) and [Kevin Beaumont](https://twitter.com/GossiTheDog) for your support and insight :)

## FAQ

#### How can I help you measure this stuff?

If you have RIPE Atlas credits, run your own analysis, do new studies, fork this hacked-together code, have fun with it!

If you have spare RIPE Atlas credits that you don't want/need, I'd certainly appreciate any credit donation you can spare if I restart measurements! Reach out to me on [Twitter](https://twitter.com/_tweedge) or [Reddit](https://www.reddit.com/user/tweedge) if that's the case and I'll send you my RIPE Atlas email.

#### How can I get involved in other ways?

Read over the resources [here](https://www.npr.org/2022/02/25/1082992947/ukraine-support-help). Spread factual information about the invasion - even take the time to fact-check yourself before you post. Accept that many Russians do not want this. Practice compassion. There are thousands of soldiers dying on both sides at a politicians' whim again.

#### I meant how can I get involved in *hacktivism*.

I'm not going to tell you that.

#### Why did you make a snide comment about websites that "DDoS" people earlier?

They're low throughput compared to any real DDoS tool, they're especially easy to neuter (site operators can disable all [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) requests by denying the HTTP OPTIONS method, and you shouldn't disable CORS in your browser to bypass this...), several are made anonymously (and who knows if your IP/information is being logged straight to the Kremlin), etc. It's not a good way to get involved.

#### How are you connecting to a specific TCP port using RIPE Atlas?

It's a "TCP Ping" - using traceroute with TCP instead of the usual ICMP. You can see this workaround described by Vesna Manojlovic in [Measuring Reachability of your Web Server using RIPE Atlas](https://www.ripe.net/support/training/ripe-ncc-educa/presentations/measuring-reachability-of-your-web-server-using-ripe-atlas.pdf) - it's a neat trick.
