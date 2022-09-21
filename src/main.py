from prometheus_client import start_http_server, Summary
from prometheus_client.core import GaugeMetricFamily, REGISTRY

from senecdata import senecdata

import argparse
import time

class senecCollector(object):
    def __init__(self, ip):
        self.ip = ip
        self.data = senecdata(self.ip)

    def collect(self):
        self.data.get_data()
        yield GaugeMetricFamily('senec_state', 'Senec State', value=self.data.get_state())
        yield GaugeMetricFamily('senec_battery_power', 'Senec Battery Power', value=self.data.get_battery_power())
        yield GaugeMetricFamily('senec_inverter_power', 'Senec Inverter Power', value=self.data.get_inverter_power())
        yield GaugeMetricFamily('senec_house_power', 'Senec House Power', value=self.data.get_house_power())
        yield GaugeMetricFamily('senec_grid_power', 'Senec Grid Power', value=self.data.get_grid_power())
        yield GaugeMetricFamily('senec_battery_charge', 'Senec Battery Charge', value=self.data.get_battery_charge())
        yield GaugeMetricFamily('senec_charging_info', 'Senec Charging Info', value=self.data.get_charging_info())
        yield GaugeMetricFamily('senec_boosting_info', 'Senec Boosting Info', value=self.data.get_boosting_info())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Senec Prometheus Exporter')

    parser.add_argument('--ip', type=str, help='Senec IP', required=True)
    parser.add_argument('--port', type=int, help='Port to listen on', default=8000)
    parser.add_argument('--interval', type=float, help='Interval to refresh data in ms', default=4000)

    args = parser.parse_args()

    senec = senecCollector(args.ip)
    REGISTRY.register(senec)
    # Start up the server to expose the metrics.
    start_http_server(args.port)
    # Generate some requests.
    while True:
        time.sleep(args.interval)
        