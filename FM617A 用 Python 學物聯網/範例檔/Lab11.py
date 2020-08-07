from machine import Pin
import time
import dht

sensor = dht.DHT11(Pin(0))         # 使用 D3 腳位取得溫溼度物件
while True:
    sensor.measure()
    temp_humi = "%2d℃/%2d%%" % (
        sensor.temperature(),
        sensor.humidity())
    print(temp_humi)
    time.sleep(3)

