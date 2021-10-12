# This file is executed on every boot (including wake-boot from deepsleep)

# import asyncio  # 時刻の同期用
import ntptime
from machine import RTC
import network

import gc
gc.collect()

ntptime.host = 'ntp.nict.jp'  # Japanese NTP server


# async def getNtpTime():
#     while True:
#         print('get NTP time')
#         ntptime.settime()
#         await asyncio.sleep_ms(1000)

# Connect to Fiwi
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('\n\nconnecting to network...')
    sta_if.active(True)
    sta_if.connect('TP-Link_0AB0', '42008880')
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

#  RTC from NTC
rtc = RTC()

# 非同期で時刻を取得する
# asyncio.create_task(getNtpTime())

ntptime.settime()
