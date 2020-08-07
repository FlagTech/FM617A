# 本套件原 Lab07 的接線圖已有異動, 請參見本範例解壓縮
# 後的『FM617A勘誤.pdf』, 若造成不便之處尚祈見諒

from machine import Pin
import mfrc522, time

rfid = mfrc522.MFRC522(0, 2, 4, 5, 14)
led = Pin(15, Pin.OUT)

while True:

    led.value(0)  # 搜尋卡片之前先關閉 LED
    stat, tag_type = rfid.request(rfid.REQIDL)  # 搜尋 RFID 卡片
    
    if stat == rfid.OK:  # 找到卡片
        stat, raw_uid = rfid.anticoll()  # 讀取 RFID 卡號
        if stat == rfid.OK:
            led.value(1)  # 讀到卡號後點亮 LED
            
            # 將卡號由 2 進位格式轉換為 16 進位的字串
            id = "%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1],
                                       raw_uid[2], raw_uid[3])
            print("偵測到卡號：", id)
            
            time.sleep(0.5)  # 暫停一下, 避免 LED 太快熄滅看不到