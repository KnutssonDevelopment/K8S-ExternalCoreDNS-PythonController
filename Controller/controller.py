from kubernetes import client, config, watch
import logging
from Controller.Models.Models import ExternalDNSRecord, ExternalDNSRecord


def watch_external_dns_records():
    config.load_kube_config()
    logger = logging.getLogger('DNS WATCHER')

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
        logger.info(f"Event: {event_type} {metadata['namespace']}/{metadata['name']}")
        logger.debug(f"dnsName: {spec['dnsName']} recordType: {spec['recordType']} Values: {', '.join(spec['values'])}")

        # Do something based on the event type
        # e.g., handle the resource creation, update, or deletion



