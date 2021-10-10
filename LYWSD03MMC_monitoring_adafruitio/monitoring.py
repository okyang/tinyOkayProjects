"""
Credits/References:
1. 2021 Dan Halbert, written for Adafruit Industries
"""

import time, os
from pathlib import Path
import logging
from dotenv import load_dotenv

# this library is currently only supported on the raspberry pi
import adafruit_ble
from adafruit_ble.advertising.standard import Advertisement
from adafruit_ble_lywsd03mmc import LYWSD03MMCService

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

logging.basicConfig(
    level=logging.INFO, format=" %(asctime)s - %(levelname)s - %(message)s"
)

# load environment variables
dirname = os.path.dirname(__file__)
dotenv_path = Path(os.path.join(dirname, ".env"))
load_dotenv(dotenv_path=dotenv_path)

AFRUIT_IO_USERNAME = os.getenv("AFRUIT_IO_USERNAME")
ADAFRUIT_IO_KEY = os.getenv("ADAFRUIT_IO_KEY")
HUMIDITY_FEED = os.getenv("HUMIDITY_FEED")
TEMPERATURE_FEED = os.getenv("TEMPERATURE_FEED")

def get_sensor_telemetry(connection, loop_duration=300):
    service = connection[LYWSD03MMCService]
    client = MQTTClient(AFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

    while connection.connected:
        client.connect()  # will connect to mqtt if not connnected

        # try 3 times to get a non None value for
        # the temperature and humidity values. Once, successful, send the
        # telemetry to MQTT
        temp, humid = None, None
        for i in range(3):
            response = service.temperature_humidity
            if response:
                temp, humid = response
                logging.info(f"Temperature: {temp} | Humidity: {humid}")
                client.publish(HUMIDITY_FEED, humid)
                client.publish(TEMPERATURE_FEED, temp)
                break
            time.sleep(5)
        time.sleep(loop_duration)


def loop_job(loop_duration=300):
    # PyLint can't find BLERadio for some reason so special case it here.
    ble = adafruit_ble.BLERadio()  # pylint: disable=no-member

    connection = None

    while True:
        logging.info("Scanning...")
        for adv in ble.start_scan(Advertisement, timeout=5):
            if adv.complete_name == "LYWSD03MMC":
                try:
                    connection = ble.connect(adv)
                    logging.info("Connected")
                    break
                except Exception as e:
                    logging.info(e)

        # Stop scanning whether or not we are connected.
        ble.stop_scan()

        if connection and connection.connected:
            try:
                get_sensor_telemetry(connection, loop_duration)
            except Exception as e:
                logging.info(e)


if __name__ == "__main__":
    loop_job(300)
