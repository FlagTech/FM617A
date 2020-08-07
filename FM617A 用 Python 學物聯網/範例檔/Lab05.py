from machine import Pin
import time, network, urequests

# 連線 Wifi 網路 
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Wifi基地台", "Wifi密碼")
while not sta_if.isconnected():
    pass
print("Wifi已連上")

# 建立 16 號腳位的 Pin 物件, 設定為輸入腳位, 並命名為 shock
shock = Pin(16, Pin.IN)

while True:
    if shock.value() == 1:
        print("感應到振動!")
        
        # 連線 IFTTT 服務發送簡訊通知
        urequests.get("IFTTT的HTTP請求網址")    
        
        # 暫停 60 秒, 避免短時間內一直收到重複的警報
        time.sleep(60)
