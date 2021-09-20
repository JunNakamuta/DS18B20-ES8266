import ssd1306
from machine import Pin, I2C
import time
import ds18x20
import onewire

# SSD1306 OLED display

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hello, World!', 0, 0, 1)
display.show()


ow = onewire.OneWire(Pin(0))  # GPIO5 で OneWire バスを作成
ds = ds18x20.DS18X20(ow)
# roms = ds.scan()
# ds.convert_temp()
# time.sleep_ms(750)
# for rom in roms:
#     print(ds.read_temp(rom))

while(True):
    roms = ds.scan()
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print('Temp:[%03.02f]C ' % ds.read_temp(rom), end='\n')

    led = Pin(13, Pin.OUT)
    led.on()
    time.sleep(1)
    led.off()
