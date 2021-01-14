import RPi.GPIO as GPIO
import random

import os
import mouse
from time import sleep
from pynput.mouse import Button, Controller
mouse = Controller()

import pyautogui

page = 6

buttons = [False,False,False,False,False,False,False,False,False]

def menuHan(channel, button):
    global page
    
    print("Button "+str(button))
    print(random.randint(1,1000))
    
    if buttons[2]:
        if button < 3:
            page = button
        else:
            page = button-1
        return "page sel"
        
    if GPIO.input(channel):
        print("up")
        buttons[button-1] = False
        return "up"
    else:
        if buttons[button-1]:
            print("up (caught)")
            buttons[button-1] = False
            return "up"
        else:
            print("down")
            buttons[button-1] = True
            return "down"

def button_callback1(channel):
    motion = menuHan(channel, 1)
    
    global page
    
    if motion == "down":
        if page is 1:
            pyautogui.press('q')
            
        elif page is 2:
            pyautogui.press('b')
        
        elif page is 3:
            pyautogui.press('d')
        
        elif page is 4:
            pyautogui.press('s')
        
        elif page is 8:
            os.system('notify-send "blocked mode"')
            sleep(10)
            os.system('pkill dis.sh')
            os.system('pkill psp.sh')
			sleep(1)
            os.system('pkill python3')
    
def button_callback2(channel):
    motion = menuHan(channel, 2)
    
    global page
    
    if motion == "down":
        if page is 1:
            pyautogui.press('u')
            
        elif page is 2:
            pyautogui.press('r')
        
        elif page is 3:
            pyautogui.press('j')
        
        elif page is 4:
            pyautogui.press('v')
    
def button_callback3(channel):
    print("Button 3")
    print(random.randint(1,1000))
    
    if GPIO.input(channel):
        print("Menu Closed")
        buttons[2] = False
    else:
        if buttons[2]:
            print("Menu Closed (caught)")
            buttons[2] = False
        else:
            print("Menu Opened")
            buttons[2] = True
    
def button_callback4(channel):
    motion = menuHan(channel, 4)
    
    global page
    
    if motion == "down":
        if page is 1:
            pyautogui.press('i')
            
        elif page is 2:
            pyautogui.press('o')
        
        elif page is 3:
            pyautogui.press('h')
            
def button_callback5(channel):
    motion = menuHan(channel, 5)
    
    global page
    
    if motion == "down":
        if page is 1:
            pyautogui.press('c')
            
        elif page is 2:
            pyautogui.press('w')
        
        elif page is 3:
            pyautogui.press('m')

    
def button_callback6(channel):
    motion = menuHan(channel, 7)
    
    global page
    
    if motion == "down":
        if page is 1:
            pyautogui.press('g')
            
        elif page is 2:
            pyautogui.press('f')
        
        elif page is 3:
            pyautogui.press('l')
            
    if page is 6:
        if motion == "up":
            print("Mouse up")
            mouse.release(Button.left)
        else:
            print("Mouse down")
            mouse.press(Button.left)

def button_callback7(channel):
    motion = menuHan(channel, 6)
    
    if motion == "down":
        if page is 1:
            pyautogui.press('k')
            
        elif page is 2:
            pyautogui.press('n')
        
        elif page is 3:
            pyautogui.press('p')
            
    
def button_callback8(channel):
    motion = menuHan(channel, 8)
    
    if motion == "down":
        if page is 1:
            pyautogui.press('e')
            
        elif page is 2:
            pyautogui.press('a')
        
        elif page is 3:
            pyautogui.press('z')
    
def button_callback9(channel):
    motion = menuHan(channel, 9)

    if motion == "down":
        if page is 1:
            pyautogui.press('t')
            
        elif page is 2:
            pyautogui.press('x')
        
        elif page is 3:
            pyautogui.press('y')
    
    if page is 6:
        if motion == "up":
            print("RMB Mouse up")
            mouse.release(Button.right)
        else:
            print("RMB Mouse down")
            mouse.press(Button.right)
            
            
"""
-=- Pages -=-

_ = nothing

[M] = Page selector - hold and press another button to select page


page selector:

1 2 [M]

3 4 5

6 7 8

---page 1---

q u [M]

i c k

g e t

---page 2---

b r [M]

o w n 

f a x

---page 3---

d j [M]

h m p

l z y

---page 4---

s v [M]

_ _ _

_ _ _

---page 7---

_ _ _

_ _ _

LMB _ RMB

---page 9---

[kill] _ _

_ _ _

_ _ _

"""
            
            
#GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)

bounce = 100 #delay between detecting events on the same button. Too low = bouncing, too high = lost inputs

GPIO.add_event_detect(36,GPIO.BOTH,callback=button_callback1, bouncetime=bounce)
GPIO.add_event_detect(22,GPIO.BOTH,callback=button_callback2, bouncetime=bounce)
GPIO.add_event_detect(18,GPIO.BOTH,callback=button_callback3, bouncetime=bounce)
GPIO.add_event_detect(16,GPIO.BOTH,callback=button_callback4, bouncetime=bounce)
GPIO.add_event_detect(37,GPIO.BOTH,callback=button_callback5, bouncetime=bounce)
GPIO.add_event_detect(29,GPIO.BOTH,callback=button_callback6, bouncetime=bounce)
GPIO.add_event_detect(31,GPIO.BOTH,callback=button_callback7, bouncetime=bounce)
GPIO.add_event_detect(40,GPIO.BOTH,callback=button_callback8, bouncetime=bounce)
GPIO.add_event_detect(38,GPIO.BOTH,callback=button_callback9, bouncetime=bounce)


#nohup skips input so using input to block the program from ending will not work
sleep(9999999)

#36,22,18,16,37,29,31,40,38
