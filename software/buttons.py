import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import random

import os
import mouse
from time import sleep
from pynput.mouse import Button, Controller
mouse = Controller()

import pyautogui

count = 0
mouseLeftDown = False

def button_callback1(channel):
    print("Button 1")
    print(random.randint(1,1000))
def button_callback2(channel):
    print("Button 2")
    print(random.randint(1,1000))
def button_callback3(channel):
    print("Button 3")
    print(random.randint(1,1000))
    os.system('notify-send "pkill python3 - button.py"')
    os.system('pkill python3')
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
    global count
    count = count + 0.5
    print(count)
    
def button_callback9(channel):
    global mouseLeftDown
    
    if GPIO.input(channel):
        print("Button 9 up")
        #print(random.randint(1,1000))
        #pyautogui.click()
        mouse.release(Button.left)
        mouseLeftDown = False
    else:
        if mouseLeftDown:
            print("Button 9 down (caught as up)")
            #print(random.randint(1,1000))
            #pyautogui.click()
            mouse.release(Button.left)
            mouseLeftDown = False
        else:
            print("Button 9 down")
            #print(random.randint(1,1000))
            #pyautogui.click()
            mouse.press(Button.left)
            mouseLeftDown = True
#GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)

bounce = 100

# Setup event on pin 10 rising edge
GPIO.add_event_detect(36,GPIO.BOTH,callback=button_callback1, bouncetime=bounce)
GPIO.add_event_detect(22,GPIO.BOTH,callback=button_callback2, bouncetime=bounce)
GPIO.add_event_detect(18,GPIO.BOTH,callback=button_callback3, bouncetime=bounce)
GPIO.add_event_detect(16,GPIO.BOTH,callback=button_callback4, bouncetime=bounce)
GPIO.add_event_detect(37,GPIO.BOTH,callback=button_callback5, bouncetime=bounce)
GPIO.add_event_detect(29,GPIO.BOTH,callback=button_callback6, bouncetime=bounce)
GPIO.add_event_detect(31,GPIO.BOTH,callback=button_callback7, bouncetime=bounce)
GPIO.add_event_detect(40,GPIO.BOTH,callback=button_callback8, bouncetime=bounce)
GPIO.add_event_detect(38,GPIO.BOTH,callback=button_callback9, bouncetime=bounce)


#message = input("Press enter to quit\n\n") # Run until someone presses enter
sleep(999999)

GPIO.cleanup() # Clean up



#36,22,18,16,37,29,31,40,38 
