import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import random

def button_callback1(channel):
    print("Button 1")
    print(random.randint(1,1000))
def button_callback2(channel):
    print("Button 2")
    print(random.randint(1,1000))
def button_callback3(channel):
    print("Button 3")
    print(random.randint(1,1000))
def button_callback4(channel):
    print("Button 4")
    print(random.randint(1,1000))
def button_callback5(channel):
    print("Button 5")
    print(random.randint(1,1000))
def button_callback6(channel):
    print("Button 7")
    print(random.randint(1,1000))
def button_callback7(channel):
    print("Button 6")
    print(random.randint(1,1000))
def button_callback8(channel):
    print("Button 8")
    print(random.randint(1,1000))
def button_callback9(channel):
    print("Button 9")
    print(random.randint(1,1000))

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)
"""

# Setup event on pin 10 rising edge
GPIO.add_event_detect(36,GPIO.RISING,callback=button_callback1)
GPIO.add_event_detect(22,GPIO.RISING,callback=button_callback2)
GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback3)
GPIO.add_event_detect(16,GPIO.RISING,callback=button_callback4)
GPIO.add_event_detect(37,GPIO.RISING,callback=button_callback5)
GPIO.add_event_detect(29,GPIO.RISING,callback=button_callback6)
GPIO.add_event_detect(31,GPIO.RISING,callback=button_callback7)
GPIO.add_event_detect(40,GPIO.RISING,callback=button_callback8)
GPIO.add_event_detect(38,GPIO.RISING,callback=button_callback9)
"""
GPIO.add_event_detect(36,GPIO.FALLING,callback=button_callback1)
GPIO.add_event_detect(22,GPIO.FALLING,callback=button_callback2)
GPIO.add_event_detect(18,GPIO.FALLING,callback=button_callback3)
GPIO.add_event_detect(16,GPIO.FALLING,callback=button_callback4)
GPIO.add_event_detect(37,GPIO.FALLING,callback=button_callback5)
GPIO.add_event_detect(29,GPIO.FALLING,callback=button_callback6)
GPIO.add_event_detect(31,GPIO.FALLING,callback=button_callback7)
GPIO.add_event_detect(40,GPIO.FALLING,callback=button_callback8)
GPIO.add_event_detect(38,GPIO.FALLING,callback=button_callback9) 
"""

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up



#36,22,18,16,37,29,31,40,38 