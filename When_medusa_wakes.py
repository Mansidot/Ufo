from machine import Pin
import time
#defining pins to be inputs and outputs
Sensor=Pin(4, Pin.IN)
led1=Pin(5,Pin.OUT)
led2=Pin(18,Pin.OUT)
while(True):
    sensorValue=Sensor.value()
    if sensorValue==1:
        #do something
        led1.value(1)
        led2.value(1)
        time.sleep(10)
        led1.value(0)
        led2.value(0)
        time.sleep(1)
    if sensorValue==0:
        #do something
        led1.value(0)
        led2.value(0)

