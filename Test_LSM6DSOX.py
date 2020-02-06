'''
Installation Notes:

sudo apt-get install libusb-1.0 libudev-dev
Use a text editor to create and edit the file
/etc/udev/rules.d/99-mcp2221.rules and add the following contents.
SUBSYSTEM=="usb", ATTRS{idVendor}=="04d8", ATTR{idProduct}=="00dd", MODE="0666"

pip3 install hidapi

pip3 install adafruit-blinka

set environment parameter and start python/idle
BLINKA_MCP2221=1
idle3

'''
import time
import board
import busio
from adafruit_lsm6ds import LSM6DSOX
device = hid.device()
device.open(0x04D8, 0x00DD)
print(os.environ["BLINKA_MCP2221"])
i2c = busio.I2C(board.SCL, board.SDA)

sensor = LSM6DSOX(i2c)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s" % (sensor.gyro))
    print("")
    time.sleep(0.5)
