from machine import Pin
import time

red = Pin(18,Pin.OUT)
green = Pin(19,Pin.OUT)
amber = Pin(20,Pin.OUT)

#Number of iterations for the  while loop 
counter = 0

while counter < 10 :
    print(counter)
    
    # Turn the leds on 
    red.value(1)
    green.value(0)
    amber.value(0)
    
    # Wait for half a second 
    time.sleep(0.5)
    
    #Leds on 
    red.value(0)
    green.value(1)
    amber.value(0)
    
    time.sleep(0.5)
    
    red.value(0)
    green.value(0)
    amber.value(1)
    
    time.sleep(0.5)
    
    
    counter +=1

amber.value(0) #Turn off after the loop 
    