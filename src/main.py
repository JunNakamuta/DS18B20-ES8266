import time
from machine import Pin, I2C
import ds18x20
import onewire
import ssd1306

LED_PIN = 2  # Arduino: D4

# SSD1306 OLED display
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 32, i2c)
display.invert(False)

ow = onewire.OneWire(Pin(0))  # GPIO5 で OneWire バスを作成
ds = ds18x20.DS18X20(ow)

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
        display.text('Temperature:', 2, 2, 1)
        display.text(Message, 2, 14, 1)
        display.show()

    led = Pin(LED_PIN, Pin.OUT)
    led.off()
    led.on()
    time.sleep(1)
