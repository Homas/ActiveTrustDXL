# ActiveTrust Dossier/TIDE API DXL Service
[![OpenDXL Bootstrap](https://img.shields.io/badge/Built%20With-OpenDXL%20Bootstrap-blue.svg)](https://github.com/opendxl/opendxl-bootstrap-python)

## Overview
The ActiveTrust DXL service exposes access to the ActiveTrust TIDE/Dossier API via the Data Exchange Layer (DXL) fabric.

## Documentation
TODO: Provide documentation information

## Installation
To start using the ActiveTrust Dossier/TIDE API DXL Service:

* Download the [Latest Release](https://github.com/Homas/ActiveTrustDXL/releases/latest)
* Extract the release .zip file
* View the `README.html` file located at the root of the extracted files.
  * The `README` links to the documentation which includes installation instructions and usage examples.

## Docker Support
A pre-built Docker image can be used as an alternative to installing a Python environment with the modules required for the VirusTotal DXL service.
See the [Wiki](https://github.com/Homas/ActiveTrustDXL/wiki) for details.

## Running
Once the application library has been installed and the configuration files are populated it can be started by executing the following command line:
```
python -m activetrustlookup <configuration-directory>
```
The <configuration-directory> argument must point to a directory containing the configuration files required for the application.
For example:
```
python -m activetrustlookup config
```

## Usage examples
Topic:
```
/infoblox/activetrust/tide
```
Request:
```
{
  "type":"host",
  "host":"eicar.top",
  "data_format":"json"
}
```
Response:
```
{
    "dropped": false,
    "dropped_record_count": 0,
    "filtered_record_count": 1,
    "record_count": 1,
    "threat": [
        {
            "batch_id": "107cc736-a6d0-11e6-a1f8-8bafd3774c57",
            "class": "MalwareC2",
            "detected": "2016-11-09T22:58:44.142Z",
            "dga": "false",
            "domain": "eicar.top",
            "expiration": "2038-01-19T22:58:44.142Z",
            "host": "eicar.top",
            "id": "107d1557-a6d0-11e6-a1f8-8bafd3774c57",
            "imported": "2016-11-09T22:58:44.142Z",
            "ip": "",
            "origin": "",
            "profile": "IID",
            "property": "MalwareC2_Generic",
            "received": "2016-11-09T22:58:44.142Z",
            "target": "",
            "threat_level": 100,
            "tld": "top",
            "tlp": "",
            "type": "HOST",
            "up": "true",
            "url": ""
        }
    ]
}
```

Topic:
```
/infoblox/activetrust/tide_lookup
```
Request:
```
{
  "data":"8.8.8.8"
}
```
Response:
```
{
    "dropped": false,
    "dropped_record_count": 1,
    "filtered_record_count": 0,
    "record_count": 1,
    "threat": []
}
```

Topic:
```
/infoblox/activetrust/dossier
```
Request:
```
{"target":
  {"one":
    {"type":"host",
     "target": "example.com",
     "sources": ["alexa","whois"]
    }
  }
}
```
Response:
```
{
    "job": {
        "completed_tasks": [
            "e7bc626b-b9b1-4440-85c6-b75910c60375",
            "4cafcf98-e76e-43fe-9dde-f04cd0ff8b31"
        ],
        "create_time": "2017-11-20T12:29:44.615Z",
        "create_ts": 1511180984615,
        "id": "786cd2ee-8e5c-4d17-b21a-94301b6c8217",
        "org": "InfoBlox",
        "state": "completed",
        "status": "success",
        "user": "vpavlov@infoblox.com"
    },
    "job_id": "786cd2ee-8e5c-4d17-b21a-94301b6c8217",
    "results": [
        {
            "data": {
                "details": {
                    "rank": 15854
                },
                "match": true
            },
            "params": {
                "source": "alexa",
                "target": "example.com",
                "type": "host"
            },
            "status": "success",
            "task_id": "e7bc626b-b9b1-4440-85c6-b75910c60375",
            "v": "2.0.1"
        },
        {
            "data": {
                "response": {
                    "domain_name": "example.com",
                    "name_servers": [
                        "A.IANA-SERVERS.NET",
                        "B.IANA-SERVERS.NET"
                    ],
                    "parsed_whois": {
                        "contacts": {
                            "admin": {
                                "city": "",
                                "country": "",
                                "email": "",
                                "fax": "",
                                "name": "",
                                "org": "",
                                "phone": "",
                                "postal": "",
                                "state": "",
                                "street": []
                            },
                            "billing": {
                                "city": "",
                                "country": "",
                                "email": "",
                                "fax": "",
                                "name": "",
                                "org": "",
                                "phone": "",
                                "postal": "",
                                "state": "",
                                "street": []
                            },
                            "registrant": {
                                "city": "",
                                "country": "",
                                "email": "",
                                "fax": "",
                                "name": "",
                                "org": "Internet Assigned Numbers Authority",
                                "phone": "",
                                "postal": "",
                                "state": "",
                                "street": []
                            },
                            "tech": {
                                "city": "",
                                "country": "",
                                "email": "",
                                "fax": "",
                                "name": "",
                                "org": "",
                                "phone": "",
                                "postal": "",
                                "state": "",
                                "street": []
                            }
                        },
                        "created_date": "1992-01-01T00:00:00",
                        "domain": "example.com",
                        "expired_date": "",
                        "name_servers": [],
                        "other_properties": {
                            "source": "IANA"
                        },
                        "registrar": {
                            "abuse_contact_email": "",
                            "abuse_contact_phone": "",
                            "iana_id": "",
                            "name": "",
                            "url": "",
                            "whois_server": ""
                        },
                        "statuses": [],
                        "updated_date": ""
                    },
                    "record_source": "example.com",
                    "registrant": "Internet Assigned Numbers Authority",
                    "registration": {
                        "created": "1995-08-14",
                        "expires": "2018-08-13",
                        "registrar": "RESERVED-Internet Assigned Numbers Authority",
                        "statuses": [
                            "clientDeleteProhibited",
                            "clientTransferProhibited",
                            "clientUpdateProhibited"
                        ],
                        "updated": "2017-08-14"
                    },
                    "whois": {
                        "date": "2017-11-18",
                        "record": "domain:       EXAMPLE.COM\n\norganisation: Internet Assigned Numbers Authority\n\ncreated:      1992-01-01\nsource:       IANA\n"
                    }
                }
            },
            "params": {
                "source": "whois",
                "target": "example.com",
                "type": "host"
            },
            "status": "success",
            "task_id": "4cafcf98-e76e-43fe-9dde-f04cd0ff8b31",
            "time": 104,
            "v": "2.0.0"
        }
    ],
    "status": "success",
    "tasks": {
        "4cafcf98-e76e-43fe-9dde-f04cd0ff8b31": {
            "create_time": "2017-11-20T12:29:44.615Z",
            "create_ts": 1511180984615,
            "end_time": "2017-11-20T12:29:45.022Z",
            "end_ts": 1511180985022,
            "id": "4cafcf98-e76e-43fe-9dde-f04cd0ff8b31",
            "params": {
                "source": "whois",
                "target": "example.com",
                "type": "host"
            },
            "start_time": "2017-11-20T12:29:44.916Z",
            "start_ts": 1511180984916,
            "state": "completed",
            "status": "success"
        },
        "e7bc626b-b9b1-4440-85c6-b75910c60375": {
            "create_time": "2017-11-20T12:29:44.615Z",
            "create_ts": 1511180984615,
            "end_time": "2017-11-20T12:29:44.917Z",
            "end_ts": 1511180984917,
            "id": "e7bc626b-b9b1-4440-85c6-b75910c60375",
            "params": {
                "source": "alexa",
                "target": "example.com",
                "type": "host"
            },
            "start_time": "2017-11-20T12:29:44.916Z",
            "start_ts": 1511180984916,
            "state": "completed",
            "status": "success"
        }
    }
}
```

Topic:
```
/infoblox/activetrust/dossier_lookup
```
Request:
```
{
  "type":"hash",
  "data":"5d7583d80e5314ac844eedc6d68c6cd7"
}
```
Response:
```
{
    "status": "success",
    "job_id": "a87877b6-3bfe-41de-aa14-869b929b1ebd",
    "job": {
        "id": "a87877b6-3bfe-41de-aa14-869b929b1ebd",
        "state": "completed",
        "status": "success",
        "create_ts": 1511181132740,
        "create_time": "2017-11-20T12:32:12.74Z",
        "completed_tasks": [
            "4fd29bcd-d283-4517-9992-a4df807f4347",
            "4ce6fa23-ee56-4d34-97bf-1a35e122e92a",
            "a9a52aab-1bd3-4b90-9f97-c50a9ae11817",
            "2c2745d6-c6d3-450c-97ca-82ca5e2e8d4c"
        ],
        "org": "InfoBlox",
        "user": "vpavlov@infoblox.com"
    },
    "tasks": {
        "2c2745d6-c6d3-450c-97ca-82ca5e2e8d4c": {
            "id": "2c2745d6-c6d3-450c-97ca-82ca5e2e8d4c",
            "state": "completed",
            "status": "success",
            "create_ts": 1511181132740,
            "create_time": "2017-11-20T12:32:12.74Z",
            "start_ts": 1511181133170,
            "start_time": "2017-11-20T12:32:13.17Z",
            "end_ts": 1511181134063,
            "end_time": "2017-11-20T12:32:14.063Z",
            "params": {
                "type": "hash",
                "target": "5d7583d80e5314ac844eedc6d68c6cd7",
                "source": "rlabs"
            }
        },
        "4ce6fa23-ee56-4d34-97bf-1a35e122e92a": {
            "id": "4ce6fa23-ee56-4d34-97bf-1a35e122e92a",
            "state": "completed",
            "status": "success",
            "create_ts": 1511181132740,
            "create_time": "2017-11-20T12:32:12.74Z",
            "start_ts": 1511181133169,
            "start_time": "2017-11-20T12:32:13.169Z",
            "end_ts": 1511181133170,
            "end_time": "2017-11-20T12:32:13.17Z",
            "params": {
                "type": "hash",
                "target": "5d7583d80e5314ac844eedc6d68c6cd7",
                "source": "isight"
            }
        },
        "4fd29bcd-d283-4517-9992-a4df807f4347": {
            "id": "4fd29bcd-d283-4517-9992-a4df807f4347",
            "state": "completed",
            "status": "success",
            "create_ts": 1511181132740,
            "create_time": "2017-11-20T12:32:12.74Z",
            "start_ts": 1511181133169,
            "start_time": "2017-11-20T12:32:13.169Z",
            "end_ts": 1511181133169,
            "end_time": "2017-11-20T12:32:13.169Z",
            "params": {
                "type": "hash",
                "target": "5d7583d80e5314ac844eedc6d68c6cd7",
                "source": "malware_analysis"
            }
        },
        "a9a52aab-1bd3-4b90-9f97-c50a9ae11817": {
            "id": "a9a52aab-1bd3-4b90-9f97-c50a9ae11817",
            "state": "completed",
            "status": "success",
            "create_ts": 1511181132740,
            "create_time": "2017-11-20T12:32:12.74Z",
            "start_ts": 1511181133169,
            "start_time": "2017-11-20T12:32:13.169Z",
            "end_ts": 1511181133171,
            "end_time": "2017-11-20T12:32:13.171Z",
            "params": {
                "type": "hash",
                "target": "5d7583d80e5314ac844eedc6d68c6cd7",
                "source": "atp"
            }
        }
    },
    "results": [
        {
            "task_id": "4fd29bcd-d283-4517-9992-a4df807f4347",
            "params": {
                "type": "hash",
                "target": "5d7583d80e5314ac844eedc6d68c6cd7",
                "source": "malware_analysis"
            },
            "v": "2.0.2",
            "status": "success",
            "time": 232,
            "data": {
                "details": {
                    "av_engine_count": 55,
                    "av_match_count": 0,
                    "av_scan_time": "2016-11-25 10:56:59",
                    "av_scans": {
                        "ALYac": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.0.1.9"
                        },
                        "AVG": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "16.0.0.4664"
                        },
                        "AVware": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.5.0.42"
                        },
                        "Ad-Aware": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "3.0.3.794"
                        },
                        "AegisLab": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "4.2"
                        },
                        "AhnLab-V3": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "3.8.1.16042"
                        },
                        "Antiy-AVL": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.0.0.1"
                        },
                        "Arcabit": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.0.0.788"
                        },
                        "Avast": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "8.0.1489.320"
                        },
                        "Avira": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "8.3.3.4"
                        },
                        "Baidu": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.0.0.2"
                        },
                        "BitDefender": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "7.2"
                        },
                        "Bkav": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161124",
                            "version": "1.3.0.8455"
                        },
                        "CAT-QuickHeal": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "14.00"
                        },
                        "CMC": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.1.0.977"
                        },
                        "ClamAV": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "0.99.2.0"
                        },
                        "Comodo": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "26160"
                        },
                        "Cyren": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "5.4.16.7"
                        },
                        "DrWeb": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "7.0.23.8290"
                        },
                        "ESET-NOD32": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "14501"
                        },
                        "Emsisoft": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "4.0.0.799"
                        },
                        "F-Prot": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "4.7.1.166"
                        },
                        "F-Secure": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "11.0.19100.45"
                        },
                        "Fortinet": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "5.4.233.0"
                        },
                        "GData": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "25"
                        },
                        "Ikarus": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "T3.2.1.16.0"
                        },
                        "Jiangmin": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161124",
                            "version": "16.0.100"
                        },
                        "K7AntiVirus": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "9.245.21623"
                        },
                        "K7GW": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "9.245.21625"
                        },
                        "Kaspersky": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "15.0.1.13"
                        },
                        "Kingsoft": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "2013.8.14.323"
                        },
                        "Malwarebytes": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "2.1.1.1115"
                        },
                        "McAfee": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "6.0.6.653"
                        },
                        "McAfee-GW-Edition": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "v2015"
                        },
                        "MicroWorld-eScan": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "12.0.250.0"
                        },
                        "Microsoft": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.1.13303.0"
                        },
                        "NANO-Antivirus": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.0.70.13328"
                        },
                        "Panda": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161124",
                            "version": "4.6.4.2"
                        },
                        "Qihoo-360": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.0.0.1120"
                        },
                        "Rising": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "28.0.0.1"
                        },
                        "SUPERAntiSpyware": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "5.6.0.1032"
                        },
                        "Sophos": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "4.98.0"
                        },
                        "Symantec": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "20151.1.1.4"
                        },
                        "Tencent": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.0.0.1"
                        },
                        "TheHacker": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161124",
                            "version": "6.8.0.5.1151"
                        },
                        "TotalDefense": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "37.1.62.1"
                        },
                        "TrendMicro": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "9.740.0.1012"
                        },
                        "TrendMicro-HouseCall": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "9.900.0.1004"
                        },
                        "VBA32": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161124",
                            "version": "3.12.26.4"
                        },
                        "VIPRE": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "54028"
                        },
                        "ViRobot": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "2014.3.20.0"
                        },
                        "Yandex": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161124",
                            "version": "5.5.1.3"
                        },
                        "Zillya": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161124",
                            "version": "2.0.0.3134"
                        },
                        "Zoner": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "1.0"
                        },
                        "nProtect": {
                            "detected": false,
                            "result": null,
                            "update_time": "20161125",
                            "version": "2016-11-25.02"
                        }
                    },
                    "md5": "5d7583d80e5314ac844eedc6d68c6cd7",
                    "sha1": "60d5a30042baa25d112ea8b61c595c093111dd48",
                    "sha256": "fe162e301556121782e1e5334a023e94f742a3a66434812620ae41a5da5f3360"
                },
                "match": true,
                "summary": {
                    "av_engine_count": 55,
                    "av_match_count": 0,
                    "av_match_percent": 0,
                    "first_seen": "2016-11-25 10:56:59",
                    "last_seen": "2016-11-25 10:56:59",
                    "status": "UNKNOWN",
                    "threat_level": 0,
                    "trust_factor": 1
                }
            }
        },
        {
            "task_id": "4ce6fa23-ee56-4d34-97bf-1a35e122e92a",
            "params": {
                "type": "hash",
                "target": "5d7583d80e5314ac844eedc6d68c6cd7",
                "source": "isight"
            },
            "v": "2.0.2",
            "status": "success",
            "time": 370,
            "data": {
                "match": false
            }
        },
        {
            "task_id": "a9a52aab-1bd3-4b90-9f97-c50a9ae11817",
            "params": {
                "type": "hash",
                "target": "5d7583d80e5314ac844eedc6d68c6cd7",
                "source": "atp"
            },
            "v": "2.0.0",
            "status": "error",
            "reason": "unknown type type",
            "info": "md5"
        }
    ]
}
```

## Bugs and Feedback

For bugs, questions and discussions please use the [GitHub Issues](https://github.com/Homas/ActiveTrustDXL/issues).

## LICENSE

Vadim Pavlov (c)2017

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
