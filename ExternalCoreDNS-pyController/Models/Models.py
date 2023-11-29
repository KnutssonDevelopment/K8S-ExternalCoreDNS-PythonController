from kubernetes.client import CustomObjectsApi, V1ObjectMeta

class ExternalDNSRecord:
    def __init__(self, metadata: V1ObjectMeta, spec):
        self.metadata = metadata
        self.spec = spec

class ExternalDNSRecordSpec:
    def __init__(self, dnsName: str, recordType: str, values: list):
        self.dnsName = dnsName
        self.recordType = recordType
        self.values = values
