from smbus import SMBus
import time

i2cbus= SMBus(1)
time.sleep(0.1)
IMO = 0x0A
def i2c(i2carduino,angle):
    i2cbus.write_byte(i2carduino, angle)
    time.sleep(0.1)
    
