#import ipaddress
#import ssl
import wifi
import socketpool
#import time
#import busio
#import digitalio
import board
import feathers2
import json
from adafruit_bme280 import basic as adafruit_bme280
from secrets import secrets
import time
time.sleep(10)
# Create library object using our Bus I2C port
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)


wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!"%secrets["ssid"])
print("My IP address is", wifi.radio.ipv4_address)

html = """<!DOCTYPE html>
<html>
    <head> <title>Its a fucking webpage</title> </head>
    <body> <h1>It's a Fucking Webpage</h1>
        <p>On a tiny computer!</p>
    </body>
</html>
"""

pool = socketpool.SocketPool(wifi.radio)
addr = pool.getaddrinfo("0.0.0.0", 80)[0][-1]

s = socketpool.SocketPool.socket(pool)
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    bme280data = {'temp':bme280.temperature,
             'press':bme280.pressure,
             'humid':bme280.humidity}
    jsonData = json.dumps(bme280data)
    html = """
    {0}
    """.format(jsonData)
    cl, addr = s.accept()
    #print('client connected from', addr)
    response = html
    #response = json
    #print(response)
    cl.send(response)
    cl.close()