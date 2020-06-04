import paho.mqtt.client as mqtt
from datetime import datetime
import requests
from gpiozero import LED
import time 

led = LED(4)
 
url = 'https://maker.ifttt.com/trigger/motion_detected/with/key/dyPVkO39xv4p-ANYX4Shcp'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    client.subscribe("motionSystem/running")
    client.subscribe("motionSystem/stopped")
    client.subscribe("motionSystem/detected")
 
def on_message(client, userdata, msg):
 
    on_receive()
        
    print(msg.topic+" "+str(msg.payload), "inside on message")
    if (str(msg.payload) == "b'Hello system is running'"):
        print("Received message: system is running")


    if (str(msg.payload) == "b'System stopped by user!'"):
        print("Received message: system stopped ")
        exit()
    
    if (str(msg.payload) == "b'Motion has been detected!!'"):
        print("Received message: motion detected!")
        on_detect()
        
        
def on_detect():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    body = {"value1":time}
    requests.post(url, body)
    
def on_receive():
       for i in range(8):
        led.on()
        time.sleep(0.10)
        led.off()
        time.sleep(0.10)
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
 
client.loop_forever() 
