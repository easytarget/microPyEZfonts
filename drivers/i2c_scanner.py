# Scanner i2c en MicroPython | MicroPython i2c scanner
# Renvoi l'adresse en decimal et hexa de chaque device connecte sur le bus i2c
# Return decimal and hexa adress of each i2c device
# https://projetsdiy.fr - https://diyprojects.io (dec. 2017)

from time import sleep

# pins
#SDA = 4   # default esp8266 (D2 / gpio4)
#SCL = 5   # default esp8266 (D1 / gpio5)
#SDA = 21  # default esp32
#SCL = 22  # default esp32
#SDA = 28  # default rp2040
#SCL = 29  # default rp2040

# I2C
# Wiring is important, you need good connections and pullup resisitors on the lines.
#  If you see continual 'OSError: with 'ENODEV' or 'ETIMEDOUT' you can try the SoftI2C
#  function instead, it is more tolerant of timing errors.
#  You can also play with frequency and timeout values, default:
#  freq=400000, timeout= 50000

from machine import Pin, I2C, SoftI2C
#i2c=SoftI2C(sda=Pin(SDA), scl=Pin(SCL))  # rp2040/esp32 (alt)
#i2c=I2C(0,sda=Pin(SDA), scl=Pin(SCL))    # rp2040/esp32
#i2c = I2C(sda=Pin(SDA), scl=Pin(SCL))    # esp8266  (No hardware I2c..)

while True:
    print('Scan i2c bus...')
    devices = i2c.scan()

    if len(devices) == 0:
      print("No i2c device !")
    else:
      print('i2c devices found:',len(devices))

      for device in devices:
        print("Decimal address: ",device," | Hexa address: ",hex(device))
    sleep(1)
