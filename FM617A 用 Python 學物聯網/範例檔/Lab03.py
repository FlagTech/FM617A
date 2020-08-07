from machine import Pin
import time

# 建立 16 號腳位的 Pin 物件, 設定為輸入腳位, 並命名為 shock
shock = Pin(16, Pin.IN)

while True:
    # 用 value() 方法從 16 號腳位讀取按鈕輸出的高低電位
    # 然後將讀到的值用 print() 輸出
    print(shock.value())
    
    # 暫停 0.05 秒
    time.sleep(0.05)