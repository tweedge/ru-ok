# ru-ok "Are you (RU) ok?"

This is a very quick project to assess the status of Russian internet properties (via RIPE Atlas) being targeted by hacktivists. Specifically, I am evaluating every target listed in Ukraine's hacktivist "IT ARMY" Telegram group with 50 SSL probes to check for connectivity.

I wanted to check connectivity from within Russia's borders because I saw many mixed reports across Twitter and Reddit, with international parties (Americans, Ukrainians, etc.) claiming all or almost-all target sites had been knocked offline, where Russians chimed in that all sites remained online for them. Given that Russia has a sovereign internet policy and can do as much as [disconnect themselves from the internet entirely](https://www.reuters.com/technology/russia-disconnected-global-internet-tests-rbc-daily-2021-07-22/) - could Russia simply be dropping DDoS traffic at the edge of the country (ex. using their transit providers) before the traffic hit the targets?

I was partially correct - per the last run around 2022-02-27 ~19:15:00 UTC, the status of all targets is:
* **28/92** sites up worldwide (733/2205 checks passed)
* **41/92** sites up in Russia (1033/2252 checks passed)

So there is measurably higher availability for several target sites within Russia's borders, but unless traffic from known RIPE Atlas probes is also filtered (unlikely), Russia is still facing substantial outages in the face of hacktivism.
