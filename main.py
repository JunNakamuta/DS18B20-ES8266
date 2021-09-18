import time
import ds18x20
from machine import Pin
import onewire

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
        print('Temp:[%03.01f]C ' % ds.read_temp(rom), end='  ')
    print('')

    led = Pin(13, Pin.OUT)
    led.on()
    time.sleep(1)
    led.off()
