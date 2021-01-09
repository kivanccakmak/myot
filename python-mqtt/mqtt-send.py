import sys
import paho.mqtt.client as paho
from auxiliary import read_json

def main(msg):
    """
    :msg: Str
    """
    config = read_json("config.json")
    client1 = paho.Client(config["PUBLISHER_NAME"])
    client1.connect(config["BROKER_IP"], config["BROKER_PORT"])
    ret = client1.publish(config["TOPIC"], msg)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid usage")
        print("python3 mqtt-send.py <message>")
        sys.exit(1)
    main(sys.argv[1])
