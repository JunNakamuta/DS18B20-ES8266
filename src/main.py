import time
import utime
from machine import Pin, I2C
from machine import WDT
import ds18x20
import onewire
import ssd1306


LED_PIN = 2  # Arduino: D4
# JST=UTC+9
UTC_OFFSET = 9

wdt = WDT()  # esp8266ではTimeout値は設定できない
# watchDocを有効にすると、Uploadできなくなるので注意
# UploadするためにはFirmwareを再度書き込む必要がある（まっさらにする）


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
        # print('Temp:[%03.02f]C ' % temperature, end='\n')
        Message = '      {:03.3f}`C'.format(temperature)
        display.fill(0)
        display.rect(0, 0, 128, 32, 1)
        display.text('Temperature:', 2, 2, 1)
        display.text(Message, 2, 10, 1)
        JSTtime = utime.localtime(utime.mktime(
            utime.localtime()) + UTC_OFFSET*3600)
        Message = '{:02d}/{:02d} {:02d}:{:02d}:{:02d}'.format(
            JSTtime[1], JSTtime[2],
            JSTtime[3], JSTtime[4], JSTtime[5]
        )
        display.text(Message, 2, 22, 1)
        # display.hline(0, 20, random.getrandbits(1), 1)
        display.hline(0, 20, int((JSTtime[5]/60) * 128), 1)
        display.show()

    led = Pin(LED_PIN, Pin.OUT)
    led.off()
    time.sleep_ms(10)
    wdt.feed()  # WatchDoc にfeedする
    led.on()
