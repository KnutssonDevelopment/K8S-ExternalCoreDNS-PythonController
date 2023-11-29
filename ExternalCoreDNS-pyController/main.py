from kubernetes import client, config, watch
import logging
from Models.Models import ExternalDNSRecord ExternalDNSRecord

def watch_external_dns_records():
    config.load_kube_config()
    api = client.CustomObjectsApi()
    group = 'example.com'  # Change to your group
    version = 'v1'         # Change to your version
    namespace = 'default'  # Change to the namespace you want to watch, or use None for all namespaces
    plural = 'externaldnsrecords'  # Change to your plural

    w = watch.Watch()
    for event in w.stream(api.list_namespaced_custom_object, group, version, namespace, plural):
        event_type = event['type']
        obj = event['object']
        metadata = obj.get('metadata')
        spec = obj.get('spec')

        # Log the event
        logging.info(f"Event: {event_type} {metadata['namespace']}/{metadata['name']}")

        # Do something based on the event type
        # e.g., handle the resource creation, update, or deletion

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    watch_external_dns_records()
