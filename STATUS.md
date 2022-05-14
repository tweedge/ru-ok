# All-Target Statistics
* **14/21** HTTP (80) sampled target sites up in Russia
* **11/21** HTTP (80) sampled target sites up worldwide
* **24/30** HTTPS (443) sampled target sites up in Russia
* **22/30** HTTPS (443) sampled target sites up worldwide

Notes:
* I am considering a site 'up' when it passes 70% or more uptime checks.
* Not all targeted sites are guaranteed to be in in a given sample.

# Testing Individual Targets on HTTP (80)
| Sector | Domain | % Up WW | % Up RU | Remark |
|--------|--------|---------|---------|--------|
|  | `109.207.14.3` | 0% | 0% |   |
|  | `178.248.235.161` | 100% | 100% |   |
|  | `185.157.97.168` | 0% | 20% |   |
|  | `185.157.97.98` | 100% | 40% | **WEIRD** |
|  | `185.165.123.50` | 0% | 0% |   |
|  | `185.62.200.36` | 60% | 100% |   |
|  | `195.225.39.107` | 100% | 75% |   |
|  | `212.164.137.231` | 40% | 80% |   |
|  | `78.142.221.76` | 0% | 0% |   |
|  | `ca.gisca.ru` | 100% | 100% |   |
|  | `cloud.tsargrad.tv` | 40% | 40% |   |
|  | `edo.etpgpb.ru` | 0% | 100% | **INTERESTING** |
|  | `files.testing.anketolog.ru` | 80% | 100% |   |
|  | `mercury.vetrf.ru` | 40% | 75% |   |
|  | `rk72.ru` | 100% | 100% |   |
|  | `rtvi.com` | 80% | 100% |   |
|  | `www.cse.ru` | 80% | 75% |   |
|  | `www.donobuv.com` | 0% | 0% |   |
| Courier | `195.189.222.55` | 80% | 100% |   |
| Cryptocurrency | `flashobmen.com` | 100% | 100% |   |
| Social Media | `ok.ru` | 80% | 75% |   |

*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via TCP (i.e. this is *not* application layer) to port 80 with an empty payload. This checks that the port is open and responsive, but not necessarily that the service itself is functioning. However, if the connection *failed* we should reasonably expect that the service is down as well - it is rare that sites do not run HTTP, even if only to redirect to HTTPS.

# Testing Individual Targets on HTTPS (443)
| Sector | Domain | % Up WW | % Up RU | Remark |
|--------|--------|---------|---------|--------|
|  | `178.248.238.59` | 100% | 89% |   |
|  | `185.79.118.12` | 100% | 100% |   |
|  | `195.19.96.198` | 100% | 100% |   |
|  | `212.164.137.119` | 100% | 100% |   |
|  | `213.171.56.102` | 0% | 0% |   |
|  | `213.171.56.46` | 0% | 70% | **INTERESTING** |
|  | `2700790.ru` | 100% | 100% |   |
|  | `46.235.191.53` | 100% | 100% |   |
|  | `83.gosuslugi.ru` | 0% | 100% | **INTERESTING** |
|  | `brandlab.ozon.ru` | 100% | 100% |   |
|  | `eda.yandex.ru` | 100% | 100% |   |
|  | `focus-api.kontur.ru` | 100% | 100% |   |
|  | `ftp.amo.tm` | 100% | 100% |   |
|  | `gb.tektorg.ru` | 90% | 100% |   |
|  | `iecp.ru` | 100% | 100% |   |
|  | `iz.ru` | 100% | 100% |   |
|  | `jira.anketolog.ru` | 0% | 0% |   |
|  | `kazanfirst.ru` | 100% | 100% |   |
|  | `mail.anketolog.ru` | 0% | 0% |   |
|  | `portal5.cbr.ru` | 100% | 100% |   |
|  | `rolls-and-pizza.ru` | 100% | 100% |   |
|  | `sale.etprf.ru` | 0% | 100% | **INTERESTING** |
|  | `structure.mil.ru` | 0% | 0% |   |
|  | `techlab.rarus.ru` | 90% | 100% |   |
|  | `www.roseltorg.ru` | 90% | 100% |   |
|  | `www.zarplata.ru` | 100% | 100% |   |
| Media | `radiobelarus.by` | 0% | 0% |   |
| Media | `ria.ru` | 100% | 100% |   |
| Media | `uslugi27.ru` | 90% | 89% |   |
| Media | `www.stavregion.ru` | 100% | 100% |   |

*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via SSL/TLS (i.e. this is *not* application layer) to port 443 with the SNI set to the corresponding domain. This checks that the port is open and responsive *and* that a secure connection can be established, but not necessarily that the service itself is functioning. However, if the connection *failed* we may be able to expect that the service is down as well. Not all sites run HTTPS, but for those that were *previously* known to use HTTPS, this would reasonably indicate that those HTTPS services are down.

