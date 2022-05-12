# All-Target Statistics
* **37/51** HTTP (80) sampled target sites up in Russia
* **29/51** HTTP (80) sampled target sites up worldwide
* **40/50** HTTPS (443) sampled target sites up in Russia
* **32/50** HTTPS (443) sampled target sites up worldwide

Notes:
* I am considering a site 'up' when it passes 70% or more uptime checks.
* Not all targeted sites are guaranteed to be in in a given sample.

# Testing Individual Targets on HTTP (80)
| Sector | Domain | % Up WW | % Up RU | Remark |
|--------|--------|---------|---------|--------|
|  | `109.207.1.123` | 0% | 0% |   |
|  | `176.67.242.146` | 0% | 0% |   |
|  | `178.210.71.24` | 80% | 100% |   |
|  | `178.248.239.22` | 80% | 75% |   |
|  | `185.179.85.65` | 0% | 100% | **INTERESTING** |
|  | `185.183.174.114` | 0% | 0% |   |
|  | `185.215.4.14` | 100% | 100% |   |
|  | `188.127.241.219` | 80% | 100% |   |
|  | `213.171.56.148` | 0% | 0% |   |
|  | `213.59.254.7` | 20% | 0% |   |
|  | `217.175.23.242` | 0% | 0% |   |
|  | `217.175.24.200` | 0% | 0% |   |
|  | `62.76.145.81` | 20% | 100% | **INTERESTING** |
|  | `7.aviasales.ru` | 0% | 0% |   |
|  | `83.169.194.26` | 100% | 100% |   |
|  | `87.226.162.78` | 20% | 0% |   |
|  | `91.206.147.2` | 0% | 0% |   |
|  | `91.232.230.180` | 80% | 100% |   |
|  | `94.140.201.135` | 0% | 0% |   |
|  | `airport-murmansk.ru` | 100% | 100% |   |
|  | `ati.su` | 100% | 100% |   |
|  | `bankrupt.etpu.ru` | 100% | 80% |   |
|  | `ca.otc.ru` | 100% | 100% |   |
|  | `delikateska.ru` | 80% | 100% |   |
|  | `downloads.1c.ru` | 25% | 100% | **INTERESTING** |
|  | `dss2.roseltorg.ru` | 100% | 80% |   |
|  | `e-trust.gosuslugi.ru` | 100% | 33% | **WEIRD** |
|  | `etp-ets.ru` | 60% | 100% |   |
|  | `geh.etpgpb.ru` | 0% | 100% | **INTERESTING** |
|  | `gudermes.net` | 100% | 100% |   |
|  | `ivis-sso.vetrf.ru` | 0% | 0% |   |
|  | `letters.mil.ru` | 40% | 100% | **INTERESTING** |
|  | `m.lesegais.ru` | 0% | 100% | **INTERESTING** |
|  | `market.otc.ru` | 100% | 100% |   |
|  | `rosleshoz.gov.ru` | 0% | 100% | **INTERESTING** |
|  | `scloud.rostec.ru` | 80% | 75% |   |
|  | `shop-rt.com` | 80% | 80% |   |
|  | `sverdlagro.roseltorg.ru` | 80% | 100% |   |
|  | `www.b2b-energo.ru` | 100% | 100% |   |
|  | `www.e-ofd.ru` | 100% | 100% |   |
|  | `www.garsing.ru` | 80% | 100% |   |
|  | `www.sushi-profi.ru` | 100% | 100% |   |
|  | `www.wildberries.ru` | 100% | 100% |   |
|  | `yunarmy.ru` | 100% | 100% |   |
| Bookkeeping | `151.236.114.27` | 40% | 25% |   |
| Courier | `static.cdek.ru` | 100% | 100% |   |
| Finance | `belarusbank.by` | 80% | 100% |   |
| Finance | `uat-ds1.mirconnect.ru` | 60% | 100% |   |
| Industry | `magnit.ru` | 100% | 100% |   |
| Industry | `www.nornickel.com` | 100% | 100% |   |
| Industry | `www.polymetalinternational.com` | 100% | 100% |   |

*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via TCP (i.e. this is *not* application layer) to port 80 with an empty payload. This checks that the port is open and responsive, but not necessarily that the service itself is functioning. However, if the connection *failed* we should reasonably expect that the service is down as well - it is rare that sites do not run HTTP, even if only to redirect to HTTPS.

# Testing Individual Targets on HTTPS (443)
| Sector | Domain | % Up WW | % Up RU | Remark |
|--------|--------|---------|---------|--------|
|  | `109.207.5.98` | 0% | 100% | **INTERESTING** |
|  | `146.120.90.28` | 0% | 0% |   |
|  | `178.248.238.63` | 90% | 100% |   |
|  | `178.248.239.19` | 100% | 100% |   |
|  | `185.165.123.145` | 100% | 100% |   |
|  | `185.165.123.36` | 100% | 100% |   |
|  | `185.169.155.230` | 80% | 100% |   |
|  | `185.179.85.65` | 0% | 75% | **INTERESTING** |
|  | `193.187.96.13` | 90% | 100% |   |
|  | `193.93.29.82` | 0% | 89% | **INTERESTING** |
|  | `194.226.54.32` | 100% | 100% |   |
|  | `194.54.15.168` | 100% | 100% |   |
|  | `217.175.24.86` | 80% | 100% |   |
|  | `78.142.221.76` | 0% | 0% |   |
|  | `80.67.43.33` | 100% | 100% |   |
|  | `81.211.33.101` | 90% | 100% |   |
|  | `91.206.147.3` | 0% | 0% |   |
|  | `91.230.251.70` | 80% | 90% |   |
|  | `ac.atol.ru` | 100% | 100% |   |
|  | `akado.amediateka.ru` | 100% | 100% |   |
|  | `assol.vetrf.ru` | 40% | 100% | **INTERESTING** |
|  | `av.ru` | 100% | 100% |   |
|  | `bg.roseltorg.ru` | 100% | 100% |   |
|  | `billing-api-test.preprod.more.tv` | 10% | 0% |   |
|  | `bitrix24.ru` | 100% | 100% |   |
|  | `club.dns-shop.ru` | 90% | 100% |   |
|  | `docliner.taxcom.ru` | 100% | 100% |   |
|  | `ens.mil.ru` | 0% | 0% |   |
|  | `fb.rts-tender.ru` | 0% | 100% | **INTERESTING** |
|  | `file.etprf.ru` | 0% | 0% |   |
|  | `getserial.infotecs.ru` | 100% | 100% |   |
|  | `ilovesakura.ru` | 90% | 100% |   |
|  | `k-server.1-ofd.ru` | 90% | 100% |   |
|  | `osago.sberbank.ru` | 90% | 100% |   |
|  | `ponyexpress.ru` | 90% | 100% |   |
|  | `pos.rarus.ru` | 90% | 100% |   |
|  | `rad.lot-online.ru` | 0% | 100% | **INTERESTING** |
|  | `service.fsrar.ru` | 0% | 0% |   |
|  | `spezobuv.ru` | 100% | 100% |   |
|  | `streamer.wildberries.ru` | 100% | 100% |   |
|  | `university.zakazrf.ru` | 0% | 0% |   |
|  | `www.chechnya.online` | 100% | 100% |   |
|  | `www.y-center.ru` | 0% | 89% | **INTERESTING** |
| Courier | `185.165.123.206` | 90% | 100% |   |
| Courier | `84.201.145.181` | 0% | 0% |   |
| Cryptocurrency | `betatransfer.org` | 100% | 100% |   |
| Finance | `uat-ds1.mirconnect.ru` | 0% | 100% | **INTERESTING** |
| Finance | `www.gazprombank.ru` | 90% | 100% |   |
| Industry | `nangs.org` | 100% | 89% |   |
| Time | `46.17.202.70` | 0% | 0% |   |

*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via SSL/TLS (i.e. this is *not* application layer) to port 443 with the SNI set to the corresponding domain. This checks that the port is open and responsive *and* that a secure connection can be established, but not necessarily that the service itself is functioning. However, if the connection *failed* we may be able to expect that the service is down as well. Not all sites run HTTPS, but for those that were *previously* known to use HTTPS, this would reasonably indicate that those HTTPS services are down.

