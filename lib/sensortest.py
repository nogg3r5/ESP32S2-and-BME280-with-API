import time
import busio
import digitalio
import board
import feathers2
import adafruit_dotstar

# Create a DotStar instance
dotstar = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1, auto_write=True)

# Create a colour wheel index int
color_index = 0

#Import BME280 library
from adafruit_bme280 import basic as adafruit_bme280

# Create library object using our Bus I2C port
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# sensor data
bme280_data = bytearray(8)

while True:
    # Get sensor readings
    temp_val = int(bme280.temperature * 100)
    print("\nTemperature: %0.1f C" % bme280.temperature)
    humid_val = int(bme280.humidity * 100)
    print("Humidity: %0.1f %%" % bme280.humidity)
    pres_val = int(bme280.pressure * 100)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    # Wait to send the packet again
    time.sleep(5)

