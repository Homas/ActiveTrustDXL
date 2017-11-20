# ActiveTrust Dossier/TIDE API DXL Service

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
```

Topic:
```
/infoblox/activetrust/tide_lookup
```
Request:
```
{
  "type":"ip",
  "data":"8.8.8.8"
}
```
Response:
```
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
     "target": "eicar.top",
     "sources": ["alexa","atp","dns","gcs","geo","gsb","isight","malware_analysis","pdns","ptr","rlabs","rwhois","sdf","whois"]
    }
  }
}
```
Response:
```
```

Topic:
```
/infoblox/activetrust/dossier_lookup
```
Request:
```
{
  "type":"host",
  "data":"eicar.top",
  "sources": ["alexa","atp","dns","gcs","geo","gsb","isight","malware_analysis","pdns","ptr","rlabs","rwhois","sdf","whois"]
}
```
Response:
```
```

## Bugs and Feedback

For bugs, questions and discussions please use the [GitHub Issues](https://github.com/Homas/ActiveTrustDXL/issues).

## LICENSE

Vadim Pavlov (c)2017

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
