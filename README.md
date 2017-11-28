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

- `cd src`
- `sudo nodemcu-uploader upload hello.lua`

## running script

- first connect via minicom, then run the script
- `sudo minicom -D /dev/ttyUSB0 -b 115200`
- `dofile('hello.lua')`

# Connect to Wi-Fi

- `sudo minicom -D /dev/ttyUSB0 -b 115200`
- `wifi.setmode(wifi.STATION)`
- `station_cfg={}`
- `station_cfg.ssid='MySSID'`
- `station_cfg.pwd='MyPassword'`
- `wifi.sta.config(station_cfg)`

# Run *hello* HTTP-Server

# upload the server-code
- `cd src`
- `sudo nodemcu-uploader upload myhttp.lua`

# run server
- `sudo minicom -D /dev/ttyUSB0 -b 115200`
- `dofile('myhttp.lua')`

# learn nodemcu's ip address 
- `print(wifi.sta.getip())`

# send a http request
- `wget 192.168.1.102`

![ScreenShot](https://github.com/kivanccakmak/myot/blob/master/doc/figs/http.png)

# Related
- [nodemcu-firmware](https://github.com/nodemcu/nodemcu-firmware/blob/master/README.md)
- [nodemcu-documentation](https://nodemcu.readthedocs.io/en/master/)
- [luafilesystem](https://github.com/keplerproject/luafilesystem)
