from machine import Pin
import time
onboard_led = Pin(25, Pin.OUT)
onboard_led.value(1)
print("Led is on") 
time.sleep(2)
onboard_led.value(0)
print("Led is off") 
