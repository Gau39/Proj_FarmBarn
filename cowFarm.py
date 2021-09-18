import RPi.GPIO as GPIO
from time import sleep

c = 0
d=0
def sum():
    global c,d
    a = c+d
    print("Total number of Cows:",a)
    ON_Turbine(a)


def ON_Turbine(a):
    if a >= 20:
        v =5    #max voltage
        runturbine(v)
        openValve();
    else:
        v = 2;   #Assumption that there are less than 10 cows
        runTurbine1(v); #To Save energy we consider voltage based on number of cows
        openValve();
               
T=15      
def openValve():
    openValve1();
    sendToGreenHouse(T); #T is the concentration of Methane required by the greenHouse
    closeValve1();
    openValve2();
    SendToStorage();
         
def SendToStorage():
    print("Excess Methane that is not required by Greenhouse is sent to storage");
         
def sendToGreenHouse(T):
    print("Methane from Barn sent to Greenhouse");
 
def openValve1():
    print("Valve to Green House opened");
def openValve2():
    print("Valve to Storage opened");
def closeValve1():
    print("Valve to Green House closed");
def closeValve2():
    print("Valve to Storage closed");
def runturbine(v):
    print("Turbine running at max speed");
def runTurbine1(v):
    print("Turbine running");
   
def button_call_back(channel):
    print("Entry button pushed")
    global c
    c=c+1
    print(c)
    sum()
   

def button_call2_back(channel):
    print("Exit button")
    global d
    d=d-1
    print(d)
    sum()
   
   
GPIO.setmode(GPIO.BCM)

sleeptime = .1

lightPin = 4
buttonPin1 = 17
buttonPin2 = 27
GPIO.setwarnings(False)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(lightPin,True)
GPIO.add_event_detect(buttonPin1,GPIO.RISING,callback = button_call_back,bouncetime=300)
GPIO.add_event_detect(buttonPin2,GPIO.RISING,callback = button_call2_back,bouncetime=300)


try:
    while True:
        GPIO.output(lightPin, GPIO.input(buttonPin1))
        GPIO.output(lightPin, GPIO.input(buttonPin2))
        sleep(.1)
finally:
    GPIO.output(lightPin, False)
    GPIO.cleanup()