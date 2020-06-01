import RPi.GPIO as GPIO
import time
from gpiozero import LED
from tkinter import *
import tkinter.font
import threading
import requests as rq
from datetime import datetime
import paho.mqtt.publish as publish




GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
buzzer = 13
motion = 7

GPIO.setup(buzzer, GPIO.OUT)
GPIO.output(buzzer,GPIO.LOW)
GPIO.setup(motion, GPIO.IN)
GPIO.setmode(GPIO.BOARD)



isSysOn = True # this is a global var that allows us to break of the sys loop


def detect():
    
    print("here in detect func")
    def run():
        print('running')
        while (isSysOn == True):
            print("motion ", GPIO.input(motion))
            if GPIO.input(motion) == 1:
                print("motion detected")
                GPIO.output(buzzer,GPIO.HIGH)
                publish.single("motionSystem/detected", "Motion has been detected!!", hostname="test.mosquitto.org")
                time.sleep(1)
                GPIO.output(buzzer,GPIO.LOW)
                
            elif GPIO.input(motion) == 0:
                print("no motion to detect")
                
            time.sleep(1)
            
    thread = threading.Thread(target=run)  
    thread.start()
    
def turnOn():
    print("on")
    publish.single("motionSystem/running", "Hello system is running", hostname="test.mosquitto.org")
    global  isSysOn
    isSysOn = True
    detect()
    
def turnOff():
    print("off")
    publish.single("motionSystem/stopped", "System stopped by user!", hostname="test.mosquitto.org")
    global  isSysOn
    isSysOn = False
    GPIO.cleanup()

def exitSys():
    print("exited")
    GPIO.cleanup()
    win.destroy()

win = Tk() # initiating the window for our GUI
win.title("Motion Detecting system")
myFont = tkinter.font.Font(family = 'Times', size = 12, weight = "bold")

turnOnBtn = Button(win, text = "turn on system",command =turnOn,
bg = 'green', height = 1,width = 24)
turnOnBtn.pack()

turnOffBtn = Button(win, text = "turn off system",command =turnOff,
bg = 'red', height = 1,width = 15)

turnOffBtn.pack()

exitsysBtn = Button(win, text = "Exit",command =exitSys,
bg = 'red', height = 1,width = 15)
exitsysBtn.pack()

#

win.mainloop()  
