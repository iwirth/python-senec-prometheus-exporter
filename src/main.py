from prometheus_client import start_http_server, Summary
from prometheus_client.core import GaugeMetricFamily, REGISTRY

from senecdata import senecdata

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
    senec = senecCollector('your ip here')
    REGISTRY.register(senec)
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        time.sleep(4000)
        