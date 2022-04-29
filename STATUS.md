# All-Target Statistics
* **45/63** HTTP (80) sampled target sites up in Russia
* **38/63** HTTP (80) sampled target sites up worldwide
* **61/73** HTTPS (443) sampled target sites up in Russia
* **54/73** HTTPS (443) sampled target sites up worldwide

Notes:
* I am considering a site 'up' when it passes 70% or more uptime checks.
* Not all targeted sites are guaranteed to be in in a given sample.

# Testing Individual Targets on HTTP (80)
| Sector | Domain | % Up WW | % Up RU | Remark |
|--------|--------|---------|---------|--------|
|  | `141.101.233.39` | 0% | 0% |   |
|  | `178.248.239.22` | 75% | 75% |   |
|  | `185.10.60.88` | 0% | 100% | **INTERESTING** |
|  | `185.179.85.34` | 0% | 100% | **INTERESTING** |
|  | `193.0.214.30` | 75% | 100% |   |
|  | `193.104.243.114` | 100% | 100% |   |
|  | `194.226.54.42` | 80% | 100% |   |
|  | `194.54.14.119` | 75% | 20% | **WEIRD** |
|  | `2.58.68.200` | 100% | 100% |   |
|  | `213.59.254.8` | 20% | 0% |   |
|  | `217.73.60.2` | 80% | 80% |   |
|  | `44.gosuslugi.ru` | 0% | 100% | **INTERESTING** |
|  | `46.17.206.15` | 100% | 100% |   |
|  | `46.235.191.53` | 80% | 100% |   |
|  | `5.8.79.230` | 0% | 0% |   |
|  | `80.92.36.74` | 100% | 100% |   |
|  | `83.169.194.26` | 40% | 100% | **INTERESTING** |
|  | `87.226.155.212` | 80% | 80% |   |
|  | `91.213.144.19` | 20% | 0% |   |
|  | `93.174.48.173` | 0% | 0% |   |
|  | `93.93.89.153` | 75% | 100% |   |
|  | `95.131.27.119` | 80% | 75% |   |
|  | `ac.atol.ru` | 0% | 0% |   |
|  | `agents.lot-online.ru` | 100% | 100% |   |
|  | `gr.tvigle.ru` | 0% | 0% |   |
|  | `jira.boxberry.ru` | 100% | 100% |   |
|  | `m-food.ru` | 80% | 100% |   |
|  | `m.avito.ru` | 100% | 100% |   |
|  | `mobprd.aeroflot.ru` | 100% | 100% |   |
|  | `moretv-sport.preprod.more.tv` | 0% | 0% |   |
|  | `online.vtb.ru` | 60% | 60% |   |
|  | `parking.mos.ru` | 80% | 75% |   |
|  | `premiere.okko.tv` | 100% | 100% |   |
|  | `qiwi.com` | 80% | 100% |   |
|  | `rc.more.tv` | 0% | 0% |   |
|  | `report.keydisk.ru` | 80% | 25% | **WEIRD** |
|  | `rostec.ru` | 100% | 100% |   |
|  | `sberfn.ru` | 80% | 100% |   |
|  | `sedo.fss.ru` | 100% | 100% |   |
|  | `show.okko.tv` | 80% | 100% |   |
|  | `sirano.vetrf.ru` | 50% | 100% | **INTERESTING** |
|  | `taxcom.ru` | 80% | 100% |   |
|  | `vpn.evotor.ru` | 0% | 20% |   |
|  | `www.agent.okko.tv` | 80% | 100% |   |
|  | `www.okeydostavka.ru` | 100% | 100% |   |
|  | `www.promo.okko.tv` | 100% | 100% |   |
|  | `www.rigla.ru` | 100% | 100% |   |
|  | `www.sberbank.com` | 60% | 75% |   |
|  | `yamal.gazprom-neft.ru` | 0% | 0% |   |
| Courier | `service.boxberry.ru` | 100% | 100% |   |
| Finance | `91.194.226.32` | 0% | 100% | **INTERESTING** |
| Finance | `acs3.sbrf.ru` | 0% | 0% |   |
| Finance | `sber.ru` | 40% | 75% |   |
| Finance | `uat-ds2.mirconnect.ru` | 40% | 100% | **INTERESTING** |
| Freelance | `kwork.ru` | 100% | 100% |   |
| Government | `beta.fss.ru` | 0% | 0% |   |
| Government | `forum.fss.ru` | 80% | 100% |   |
| Government | `www.nalog.gov.ru` | 100% | 100% |   |
| Industry | `magnit.ru` | 80% | 75% |   |
| Media | `belarus24.by` | 0% | 25% |   |
| Media | `radiobrestfm.by` | 80% | 80% |   |
| Media | `yaplakal.com` | 100% | 100% |   |
| Time | `46.48.118.29` | 0% | 25% |   |

*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via TCP (i.e. this is *not* application layer) to port 80 with an empty payload. This checks that the port is open and responsive, but not necessarily that the service itself is functioning. However, if the connection *failed* we should reasonably expect that the service is down as well - it is rare that sites do not run HTTP, even if only to redirect to HTTPS.

# Testing Individual Targets on HTTPS (443)
| Sector | Domain | % Up WW | % Up RU | Remark |
|--------|--------|---------|---------|--------|
|  | `146.158.48.21` | 100% | 100% |   |
|  | `176.67.241.93` | 0% | 0% |   |
|  | `178.248.235.122` | 100% | 100% |   |
|  | `178.248.236.73` | 100% | 100% |   |
|  | `178.248.238.15` | 100% | 100% |   |
|  | `178.248.238.32` | 100% | 100% |   |
|  | `185.169.155.28` | 100% | 100% |   |
|  | `185.179.85.96` | 0% | 0% |   |
|  | `193.148.44.188` | 100% | 100% |   |
|  | `193.24.8.15` | 100% | 100% |   |
|  | `194.190.12.167` | 60% | 89% |   |
|  | `194.226.54.32` | 100% | 100% |   |
|  | `37.16.85.182` | 0% | 0% |   |
|  | `46.17.203.73` | 100% | 100% |   |
|  | `46.17.204.245` | 100% | 100% |   |
|  | `46.17.204.249` | 100% | 100% |   |
|  | `7.aviasales.ru` | 100% | 100% |   |
|  | `78.142.221.116` | 0% | 0% |   |
|  | `79.142.16.20` | 100% | 100% |   |
|  | `80.87.197.227` | 100% | 100% |   |
|  | `80.92.37.121` | 100% | 100% |   |
|  | `82.202.251.98` | 0% | 0% |   |
|  | `91.213.144.237` | 100% | 100% |   |
|  | `91.230.251.101` | 100% | 100% |   |
|  | `91.230.251.71` | 100% | 100% |   |
|  | `91.230.251.81` | 100% | 100% |   |
|  | `91.232.230.180` | 100% | 100% |   |
|  | `93.93.89.150` | 90% | 100% |   |
|  | `94.124.200.1` | 100% | 100% |   |
|  | `94.26.241.164` | 100% | 100% |   |
|  | `95.173.157.26` | 0% | 100% | **INTERESTING** |
|  | `95.173.157.45` | 0% | 100% | **INTERESTING** |
|  | `accounts.vetrf.ru` | 40% | 100% | **INTERESTING** |
|  | `delivery-club.ru` | 0% | 100% | **INTERESTING** |
|  | `etpu.ru` | 90% | 90% |   |
|  | `freeipa.beta.aviasales.ru` | 100% | 100% |   |
|  | `getserial.infotecs.ru` | 90% | 100% |   |
|  | `gis.platon.ru` | 90% | 100% |   |
|  | `gr.tvigle.ru` | 0% | 0% |   |
|  | `kb.crpt.ru` | 0% | 0% |   |
|  | `kino.1tv.ru` | 100% | 100% |   |
|  | `onpz.gazprom-neft.ru` | 100% | 100% |   |
|  | `pk.platformaofd.ru` | 100% | 100% |   |
|  | `rostelecom.ru` | 0% | 0% |   |
|  | `rsbis.ru` | 90% | 100% |   |
|  | `star-pro.ru` | 80% | 100% |   |
|  | `static.more.tv` | 100% | 100% |   |
|  | `support.online.atol.ru` | 0% | 0% |   |
|  | `update.rarus.ru` | 100% | 100% |   |
|  | `www.aviasales.ru` | 100% | 100% |   |
|  | `www.b-kontur.ru` | 89% | 100% |   |
|  | `www.bitrix24.net` | 100% | 100% |   |
|  | `www.icvibor.ru` | 100% | 100% |   |
|  | `www.kt-69.ru` | 100% | 100% |   |
|  | `www.rigla.ru` | 90% | 100% |   |
|  | `www.y-center.ru` | 0% | 89% | **INTERESTING** |
| Courier | `188.130.235.86` | 0% | 0% |   |
| Cryptocurrency | `abcobmen.com` | 100% | 89% |   |
| Cryptocurrency | `baksman.org` | 100% | 100% |   |
| Cryptocurrency | `cashbank.pro` | 100% | 100% |   |
| Finance | `uat-ds2.mirconnect.ru` | 0% | 100% | **INTERESTING** |
| Government | `ca.vks.rosguard.gov.ru` | 100% | 100% |   |
| Government | `docs.fss.ru` | 90% | 100% |   |
| Government | `wiki.fss.ru` | 100% | 100% |   |
| Government | `www.belneftekhim.by` | 100% | 100% |   |
| Government | `www.gosuslugi.ru` | 80% | 100% |   |
| Media | `bezformata.com` | 100% | 100% |   |
| Media | `grodnonews.by` | 100% | 100% |   |
| Media | `radiostalica.by` | 11% | 0% |   |
| Media | `riafan.ru` | 100% | 100% |   |
| Media | `www.belnovosti.by` | 100% | 100% |   |
| Social Media | `5.61.23.11` | 100% | 100% |   |
| Time | `217.21.220.247` | 0% | 0% |   |

*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via SSL/TLS (i.e. this is *not* application layer) to port 443 with the SNI set to the corresponding domain. This checks that the port is open and responsive *and* that a secure connection can be established, but not necessarily that the service itself is functioning. However, if the connection *failed* we may be able to expect that the service is down as well. Not all sites run HTTPS, but for those that were *previously* known to use HTTPS, this would reasonably indicate that those HTTPS services are down.

