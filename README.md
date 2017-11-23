# ActiveTrust Dossier/TIDE API DXL Service
[![OpenDXL Bootstrap](https://img.shields.io/badge/Built%20With-OpenDXL%20Bootstrap-blue.svg)](https://github.com/opendxl/opendxl-bootstrap-python)

## Overview
The ActiveTrust DXL service exposes access to the ActiveTrust TIDE/Dossier API via the Data Exchange Layer (DXL) fabric.

The supported topics:
- /infoblox/activetrust/tide
- /infoblox/activetrust/tide_lookup
- /infoblox/activetrust/dossier
- /infoblox/activetrust/dossier_lookup

`/infoblox/activetrust/dossier` and `/infoblox/activetrust/tide` topics provide AS-IS access to the ActiveTrust Dossier and
TIDE APIs. Please refer ActiveTrust documentation regarding requests formats.

`/infoblox/activetrust/dossier_lookup` and `/infoblox/activetrust/tide_lookup` topics provide simplified access to the ActiveTrust Dossier and TIDE APIs. Please refer [Sample requests](https://github.com/Homas/ActiveTrustDXL/wiki/Sample-requests) page for the details.



## Documentation
Please refer [Wiki](https://github.com/Homas/ActiveTrustDXL/wiki) page for the documentation.

## Installation
To start using the ActiveTrust Dossier/TIDE API DXL Service:

* Download the [Latest Release](https://github.com/Homas/ActiveTrustDXL/releases/latest)
* Extract the release .zip file
* View the `README.html` file located at the root of the extracted files.
  * The `README` links to the documentation which includes installation instructions and usage examples.

## Docker Support
A pre-built Docker image can be used as an alternative to installing a Python environment with the modules required for the ActiveTrust Dossier/TIDE API DXL service. The image is available on the docker hub under "activetrustdxl" name.

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


## Bugs and Feedback

For bugs, questions and discussions please use the [GitHub Issues](https://github.com/Homas/ActiveTrustDXL/issues).

## LICENSE

Vadim Pavlov (c)2017

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
