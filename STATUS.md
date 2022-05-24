# All-Target Statistics
* **18/25** HTTP (80) sampled target sites up in Russia
* **16/25** HTTP (80) sampled target sites up worldwide
* **17/21** HTTPS (443) sampled target sites up in Russia
* **15/21** HTTPS (443) sampled target sites up worldwide

Notes:
* I am considering a site 'up' when it passes 70% or more uptime checks.
* Not all targeted sites are guaranteed to be in in a given sample.

# Testing Individual Targets on HTTP (80)
| Sector | Domain | % Up WW | % Up RU | Remark |
|--------|--------|---------|---------|--------|
|  | `141.101.196.238` | 0% | 0% |   |
|  | `178.248.232.153` | 80% | 100% |   |
|  | `185.129.100.34` | 100% | 100% |   |
|  | `185.179.199.85` | 100% | 80% |   |
|  | `185.185.71.170` | 100% | 100% |   |
|  | `185.219.40.214` | 100% | 100% |   |
|  | `185.30.220.100` | 0% | 0% |   |
|  | `185.30.220.118` | 0% | 0% |   |
|  | `193.238.118.65` | 0% | 0% |   |
|  | `212.100.158.83` | 100% | 100% |   |
|  | `31.31.196.233` | 100% | 100% |   |
|  | `5.23.51.195` | 0% | 0% |   |
|  | `78.155.198.128` | 80% | 100% |   |
|  | `80.72.225.222` | 100% | 75% |   |
|  | `apiedo.etpgpb.ru` | 0% | 80% | **INTERESTING** |
|  | `dev.amo.tm` | 0% | 0% |   |
|  | `ib2.psbank.ru` | 0% | 0% |   |
|  | `lkg.mil.ru` | 100% | 100% |   |
|  | `push.notisend.ru` | 100% | 100% |   |
|  | `rostec.ru` | 100% | 100% |   |
|  | `www.kartoteka.ru` | 100% | 100% |   |
|  | `www.polkrf.ru` | 100% | 100% |   |
|  | `www.uralairlines.ru` | 100% | 100% |   |
|  | `www.yaponamatrena.ru` | 100% | 100% |   |
| Industry | `www.severstal.com` | 0% | 100% | **INTERESTING** |

*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via TCP (i.e. this is *not* application layer) to port 80 with an empty payload. This checks that the port is open and responsive, but not necessarily that the service itself is functioning. However, if the connection *failed* we should reasonably expect that the service is down as well - it is rare that sites do not run HTTP, even if only to redirect to HTTPS.

# Testing Individual Targets on HTTPS (443)
| Sector | Domain | % Up WW | % Up RU | Remark |
|--------|--------|---------|---------|--------|
|  | `146.120.90.157` | 0% | 0% |   |
|  | `185.129.103.95` | 100% | 100% |   |
|  | `213.171.56.102` | 0% | 0% |   |
|  | `217.175.23.242` | 100% | 100% |   |
|  | `223fz.rus-on.ru` | 0% | 100% | **INTERESTING** |
|  | `81.200.116.2` | 0% | 0% |   |
|  | `87.236.16.129` | 100% | 100% |   |
|  | `90.156.201.68` | 100% | 100% |   |
|  | `brobank.ru` | 90% | 100% |   |
|  | `elbank.kontur.ru` | 100% | 100% |   |
|  | `epnow.ru` | 90% | 100% |   |
|  | `its.1c.ru` | 90% | 100% |   |
|  | `online.rncb.ru` | 0% | 0% |   |
|  | `premiere.okko.tv` | 90% | 100% |   |
|  | `re-store.ru` | 90% | 100% |   |
|  | `smev3.gosuslugi.ru` | 0% | 100% | **INTERESTING** |
|  | `www.minfinchr.ru` | 90% | 100% |   |
|  | `www.superjob.ru` | 90% | 100% |   |
| Freelance | `advego.com` | 100% | 100% |   |
| Government | `es.pfrf.ru` | 90% | 100% |   |
| Government | `hosting.pfrf.ru` | 100% | 100% |   |

*Additional information:* The above data is gathered via RIPE Atlas. The measurement connects via SSL/TLS (i.e. this is *not* application layer) to port 443 with the SNI set to the corresponding domain. This checks that the port is open and responsive *and* that a secure connection can be established, but not necessarily that the service itself is functioning. However, if the connection *failed* we may be able to expect that the service is down as well. Not all sites run HTTPS, but for those that were *previously* known to use HTTPS, this would reasonably indicate that those HTTPS services are down.

