import time
from machine import Pin, I2C
import ds18x20
import onewire
import ssd1306


# SSD1306 OLED display

LED_PIN = 13

i2c = I2C(sda=Pin(4), scl=Pin(5))
#  I2Cのプルアップ
# Pin(4, Pin.OUT, Pin.PULL_UP)
# Pin(5, Pin.OUT, Pin.PULL_UP)
display = ssd1306.SSD1306_I2C(128, 32, i2c)
display.invert(False)

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
        temperature = ds.read_temp(rom)
        print('Temp:[%03.02f]C ' % temperature, end='\n')
        Message = '       {:03.2f}\'C'.format(temperature)
        display.fill(0)
        display.rect(0, 0, 128, 32, 1)
        display.text('Temperature:', 2, 1, 2)
        display.text(Message, 2, 12, 2)
        display.show()

    led = Pin(LED_PIN, Pin.OUT)
    led.on()
    time.sleep(1)
    led.off()
