# python-mqtt
send receive mqtt messages in python

# installation
sudo pip install paho-mqtt
sudo apt-get install mosquitto

# run mosquitto broker
mosquitto

# receive mqtt message by python
python3 mqtt-receive.py mytopic

# receive mqtt message from shell
mosquitto\_sub -v -t mytopic

# send mqtt message
python3 mqtt-send.py myclientid mytopic mymessage

# send mqtt message from shell
mosquitto\_pub -h 127.0.0.1 -t mytopic -m "mymessage"

