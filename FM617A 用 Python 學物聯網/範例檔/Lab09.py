# 本套件原 Lab09 的接線圖已有異動, 請參見本範例解壓縮
# 後的『FM617A勘誤.pdf』, 若造成不便之處尚祈見諒

from machine import ADC
import time

# 建立 A0 腳位的 ADC 物件, 並命名為 adc
adc = ADC(0)

while True:
    # 用 read() 方法從 A0 號腳位讀取 ADC 轉換後的數值
    # 然後將讀到的值用 print() 輸出
    print(adc.read())
    
    # 暫停 0.05 秒
    time.sleep(0.05)
