#导入引脚和时间模块 
from machine import Pin  
import time  
 
# 定义火焰传感器，led的引脚
sensor_flame = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(18, machine.Pin.OUT)
 
while True: 
      value = sensor_flame.value()
      if value == 0:
          print("ALARM! Fire detected!")
          led.value(1)
          time.sleep(0.2)
          led.value(0)
          time.sleep(0.2)         
      else:
          led.value(0) 