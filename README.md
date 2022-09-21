# python-senec-prometheus-exporter

Usage:
```
usage: main.py [-h] --ip IP [--port PORT] [--interval INTERVAL]

Senec Prometheus Exporter

options:
  -h, --help           show this help message and exit
  --ip IP              Senec IP
  --port PORT          Port to listen on
  --interval INTERVAL  Interval to refresh data in ms
```
---

Running it as a service (systemd):

Create unit file ```/etc/systemd/system/senec-collector.service```
```
[Unit]
Description=Service for reading SENEC Battery Data
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /path/to/script/main.py --ip 'youriphere'
[Install]
WantedBy=multi-user.target
```
