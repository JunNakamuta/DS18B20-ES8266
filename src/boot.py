# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import ntptime
from machine import RTC
import network
# import uos
# import machine
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
# import webrepl
# webrepl.start()
gc.collect()

# Connect to Fiwi
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('TP-Link_0AB0', '42008880')
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())

#  RTC from NTC
rtc = RTC()

ntptime.host = 'ntp.nict.jp'  # Japanese NTP server
ntptime.settime()
