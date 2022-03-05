def request_tcp_ping(domain, bill_email, port):
    return {
        "definitions": [
            {
                "target": domain,
                "af": 4,
                "timeout": 4000,
                "description": f'TCP "ping" measurement to {domain} on {port}',
                "protocol": "TCP",
                "resolve_on_probe": True,
                "packets": 3,
                "size": 0,
                "first_hop": 1,
                "max_hops": 32,
                "spread": 60,
                "port": 80,
                "paris": 16,
                "destination_option_size": 0,
                "hop_by_hop_option_size": 0,
                "dont_fragment": False,
                "skip_dns_check": True,
                "type": "traceroute",
            },
        ],
        "probes": standard_probe_requisition(),
        "is_oneoff": True,
        "bill_to": bill_email,
    }

def request_ssl(domain, bill_email):
    return {
        "definitions": [
            {
                "target": domain,
                "af": 4,
                "port": 443,
                "hostname": domain,
                "description": f"SSL measurement to {domain}",
                "resolve_on_probe": True,
                "skip_dns_check": True,
                "type": "sslcert",
            },
        ],
        "probes": standard_probe_requisition(),
        "is_oneoff": True,
        "bill_to": bill_email,
    }

def standard_probe_requisition():
    return [
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "RU",
            "requested": 10,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "BY",
            "requested": 5,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "UA",
            "requested": 3,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "PL",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "RO",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "US",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "DE",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "AU",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "CA",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "BR",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "IN",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "CN",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "JP",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "ZA",
            "requested": 1,
        },
        {
            "tags": {"include": [], "exclude": []},
            "type": "country",
            "value": "GB",
            "requested": 1,
        },
    ]