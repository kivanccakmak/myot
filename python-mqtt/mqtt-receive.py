import sys
import paho.mqtt.client as mqtt
from auxiliary import read_json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    config = read_json('config.json')
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    client.subscribe(config['TOPIC'])

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def main():
    config = read_json('config.json')

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(config['BROKER_IP'], config['BROKER_PORT'], 60)
    
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

if __name__ == "__main__":
    main()
