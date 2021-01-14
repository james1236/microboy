import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1015 as ADS

from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1015(i2c)
ads.mode = Mode.SINGLE

pspX = AnalogIn(ads, ADS.P0)
pspY = AnalogIn(ads, ADS.P1)

#input("Press enter with centered joystick to calibrate")
centerX = pspX.value
centerY = pspY.value

#import pygame
#screen = pygame.display.set_mode((300,300))
#pygame.display.flip()

"""
input("Press enter at top")
topX = pspX.value
topY = pspY.value

input("Press enter at bottom")
botX = pspX.value
botY = pspY.value

input("Press enter at left")
leftX = pspX.value
leftY = pspY.value

input("Press enter at right")
rightX = pspX.value
rightY = pspY.value

"""

"""
while 1:
    print("X: (val) (voltage)")
    print(pspX.value, pspX.voltage)
    print("Y: (val) (voltage)")
    print(pspY.value, pspY.voltage)
    print("")
"""

import mouse

while 1:
    #print("X")
    circleColor = (255,0,0)
    
    thresh = 0.075
    alive = False
    
    xval = -(pspX.value-centerX)/20000
    yval = -(pspY.value-centerY)/20000
    
    if ((abs(xval) > thresh) or (abs(yval) > thresh)):
        circleColor = (0,255,0)
        alive = True
        
    #screen.fill((255,255,255))
    #pygame.draw.circle(screen,circleColor,(int(xval*300)+150,int(yval*300)+150),5,1)
    #pygame.display.update()
    
    if (alive):
        mouse.move(xval*10, yval*10, absolute=False, duration=0)
