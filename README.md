# detect_project



### This is a project detects a motion and buzzes once detecting, after that it publish an event to a MQTT server where the client can subscribe and trigger's an IFTTT request to inform client of motion detection where the device is installed at.


### You need: - 

1- Rasberry Pi (2)
2- PIR motion sensor (1)
3- Buzzer sensor (1)
4- LED (1)

#### pip3 install paho.mqtt 
#### apt-get install tkinter


### Run detect:- 

* Connect the PIR to the raspi, where GND with pin 6 or any GND pin on the pi, and specify the GPIO pin you want to read the motion from lastly connect the VCC pin to the 5V on the pi, which is the 2nd pin.
* For the buzzer it simply takes a GND for its lower leg and the GPIO pin for the positive longer leg
* For the second pi, simply have the LED attached to it, by connecting a GPIO pin and a GND.

* let the client listen to any published event by running python3 mqtt_client.py
* run python3 detect.py for the sensor to start detecting and publishing events when needed

### Demoing detect:- 
https://www.youtube.com/watch?v=e12QQH3Wg9Y&t=14s

### prototype 

## Sources: - 
* https://core-electronics.com.au/tutorials/getting-started-with-home-automation-using-mqtt.html
