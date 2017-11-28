# myot

Playground with [nodemcu](http://www.nodemcu.com/index_en.html)

# Installation

## pre-requirements

- `sudo apt-get install minicom`

- `sudo apt-get install python-pip`

- `sudo pip install esptool`

- `sudo pip install nodemcu-uploader`

## flushing firmware
- `sudo python esptool.py --port /dev/ttyUSB0 write_flash -fm dio 0x0000 nodemcu-master-22-modules-2017-11-06-15-41-32-float.bin`

## flushing script
- `sudo nodemcu-uploader upload hello.lua`

## running script

- first connect via minicom, then run the script

- `sudo minicom -D /dev/ttyUSB0 -b 115200`

- `dofile('hello.lua')`
