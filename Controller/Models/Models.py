from kubernetes.client import CustomObjectsApi, V1ObjectMeta


class ExternalDNSRecord:
    def __init__(self, metadata: V1ObjectMeta, spec):
        self.metadata = metadata
        self.spec = spec


class ExternalDNSRecordSpec:
    def __init__(self, dns_name: str, record_type: str, values: list):
        self.dnsName = dns_name
        self.recordType = record_type
        self.values = values
