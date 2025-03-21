from machine import Pin
import time

#Defining Light Sensor and Stepper Motor Pins
lightSensor = Pin(4, Pin.IN)
IN1 = Pin(27, Pin.OUT)
IN2 = Pin(14, Pin.OUT)
IN3 = Pin(12, Pin.OUT)
IN4 = Pin(13, Pin.OUT)

#Stepper Motor Sequence
stepSeq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

#the number of steps required to deploy/retract
STEPS_TO_DEPLOY = 40960
STEPS_TO_RETRACT = 40960 #Same as deploy to ensure balance

#Counter to track detection instances
detectionCount = 0  # Starting with 0 detections

# Function to deploy legs
def legsOut():
    print("Deploying Legs...")
    for _ in range(STEPS_TO_DEPLOY):  #Rotate only for defined steps
        for step in stepSeq:
            IN1.value(step[0])
            IN2.value(step[1])
            IN3.value(step[2])
            IN4.value(step[3])
            time.sleep_ms(2)  #Small delay for smooth movement
    print("Legs Deployed!")

# Function to retract legs
def legsIn():
    print("Retracting Legs...")
    for _ in range(STEPS_TO_RETRACT):  #reverse for defined steps
        for step in reversed(stepSeq):
            IN1.value(step[0])
            IN2.value(step[1])
            IN3.value(step[2])
            IN4.value(step[3])
            time.sleep_ms(2)  #Ssall delay for smooth retraction
    print("Legs Retracted!")

# Main Loop
while True:
    sensorValue = lightSensor.value()
    #CheckING if laser is detected
    if sensorValue == 0:
        detectionCount = detectionCount + 1
        print("Laser Detected! Detection Count: {detectionCount}")
        #if the detection count is odd or even:
        if detectionCount % 2 == 1:
            legsOut()  # Deploy legs on 1st, 3rd, 5th detections
        else:
            legsIn()  # Retract legs on 2nd, 4th, 6th detections
    time.sleep(0.5)  # Small delay to avoid multiple rapid triggers
