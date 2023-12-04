# K8S-ExternalCoreDNS-PythonController
A Python Controller to handle DNS Records created with project K8S-ExternalCoreDNS.


# Python Kubernetes Controller for ExternalDNSRecord

This project contains a simple Python-based Kubernetes controller that watches for changes in `ExternalDNSRecord` custom resources and logs these events.
The ExternalDNSRecord resource is a Custom Resource Definition created to control DNS record creation in external infrastructure such as Active Directory DNS.

The resource creation (CRD) has a seperate project home here: https://github.com/KnutssonDevelopment/K8S-ExternalCoreDNS

## Description

The controller uses the Kubernetes Python client to interact with the Kubernetes API. It watches for creation, update, and deletion of `ExternalDNSRecord` custom resources in a specified namespace and logs these events for demonstration purposes.

In time is will include functionality to update AD DNS records. The updated will most likely be a PowerShell based module. 

## Prerequisites

- Python 3.x
- Access to a Kubernetes cluster
- `kubectl` configured to access your cluster

## Installation

First, clone this repository to your local machine:

```bash
git clone [URL to this repository]
cd [repository name]
```
Then, install the required Python packages:

```bash
Copy code
pip install -r requirements.txt
```

## Usage
Run the controller script with:

```bash
Copy code
python external_dns_record_controller.py
```
The script will start watching for ExternalDNSRecord events in the specified Kubernetes namespace.

## Configuration
You can modify the script to watch a different namespace or to handle different custom resource definitions as needed.

## License
MIT License

## Author
Knutsson Development

The version number in `requirements.txt` should match the version of the Kubernetes Python client that you are using. You might need to adjust it depending on the version compatibility with your Kubernetes cluster.

## Notes

- In the README.md, replace placeholders like `[URL to this repository]`, `[repository name]`, and `[Your Name]` with the actual URL, repository name, and your name or your organization's name.
- Remember to add any additional instructions or details specific to your project that users might need to know.
- The `requirements.txt` file specifies the Kubernetes Python client. If your script uses other packages, make sure to list them here as well.

### requirements.txt
kubernetes>=12.0.0
