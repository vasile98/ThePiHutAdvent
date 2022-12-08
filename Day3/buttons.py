from machine import Pin
import time

button1 = Pin(13,Pin.IN,Pin.PULL_DOWN)
button2 = Pin(8,Pin.IN,Pin.PULL_DOWN)
button3 = Pin(4,Pin.IN,Pin.PULL_DOWN)

red = Pin(18,Pin.OUT)
green = Pin(19,Pin.OUT)
amber = Pin(20,Pin.OUT)

dance =  [[1,0,0],
          [0,1,0],
          [0,0,1],
          [0,0,0]]

while True :
    time.sleep(0.2)
    
    #If pressed
    if button1.value() == 1 and button2.value() == 1:
        for arr in dance:
            red.value(arr[0])
            green.value(arr[1])
            amber.value(arr[2])
            print(arr)
            time.sleep(0.5)       
    elif button1.value() == 1:
        amber.toggle()
    elif button2.value() == 1:
        green.toggle()
    elif button3.value() == 1:
        red.toggle()
