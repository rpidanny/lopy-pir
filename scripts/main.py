# main.py -- put your code here!
import time
import json
from machine import WDT
from network import WLAN

from mqtt import MQTTClient
from pir import Pir

from config import known_nets, pir_config, adafruit
from util.wifi import connect_wifi

wdt = WDT(timeout=7000)

wl = WLAN()

client = MQTTClient("lopy-pir",
                    "io.adafruit.com",
                    user=adafruit['user'],
                    password=adafruit['apikey'],
                    port=1883)

last_time = time.time()

if __name__ == "__main__":
    pir = Pir(pir_config['input_pin'])

    client.connect()

    print(' [*] Starting PIR Monitoring...')
    while True:
        try:
            client.check_msg()
            # print("Logging PIR State: " + str(pir.get_status()))
            if time.time() - last_time > pir_config['update_interval']:
                print("Logging PIR State: " + str(pir.get_status()))
                client.publish(topic=adafruit['user'] + "/feeds/lopy_pir",
                               msg=str(pir.get_status()))
                last_time = time.time()
        except Exception as e:
            print(' [-] Failed to publish data....')
            print(' [*] Reconnecting to WIFI / MQTT.')
            print(e)
            connect_wifi(known_nets)
            client.connect()
        wdt.feed()
        time.sleep(1)
