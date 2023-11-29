from Controller.controller import watch_external_dns_records
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    watch_external_dns_records()
