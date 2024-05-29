# 导入 Pin 和 time 库.
from machine import Pin
import time

# 定义火焰传感器和led的引脚. 
sensor_flame = Pin(15, Pin.IN)
led = Pin(2, Pin.OUT)
 
while True: 
      value = sensor_flame.value()
      if value == 0:
          print("ALARM! Fire detected!") 
          led.value(1)
          time.sleep(0.5)
          led.value(0)
          time.sleep(0.5)         
      else:
          led.value(0)