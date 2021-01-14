import os

#Set screen resolution
os.system('xrandr --newmode "640x640_60.00"   32.50  640 664 728 816  640 643 653 665 -hsync +vsync')
os.system('xrandr --addmode HDMI-1 640x640_60.00')
os.system('xrandr -s 640x640_60.00')

import ST7789

disp = ST7789.ST7789(
    port=0,
    cs=0,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=17,
    rst=22,
    backlight=27
    mode=3,
    rotation=0,
    spi_speed_hz= 80 * 1000 * 1000 #120 * 1000 * 1000
)

# Initialize display.
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

import numpy as np
#import cv2
from mss import mss
from PIL import Image
import time

#Custom GUI
from PIL import ImageDraw
#from PIL import ImageFont
from PIL import ImageEnhance

#Get Mouse Pos
import mouse

sct = mss()

w, h = 640, 640 #512
monitor = {'top': 0, 'left': 0, 'width': w, 'height': h}


while 1:
    last_time = time.time()
    img = Image.frombytes('RGB', (w,h), sct.grab(monitor).rgb)
    
    ##cv2.imshow('test', cv2.cvtColor(np.array(img.resize((240,240),Image.BILINEAR)), cv2.COLOR_RGB2BGR))
    #disp.display(img.resize((240,240),Image.ANTIALIAS)) #ANTIALIAS, BILINEAR
    
    img = img.resize((240,240),Image.ANTIALIAS)
    mx, my = mouse.get_position()
    mx *= 240/w
    my *= 240/h
    
    draw = ImageDraw.Draw(img)
    draw.polygon([(mx+10, my+5),(mx, my),(mx+5, my+10)], outline=(255, 255, 255), fill=(0, 0, 0))
    
    img = ImageEnhance.Color(img).enhance(1.7)
    #img = ImageEnhance.Brightness(img).enhance(1)
    
    disp.display(img) #.rotate(-90))
    
    fps = round((1 / (time.time() - last_time)) * 10) / 10
    
    print("fps: {}".format(fps))
    #os.system("notify-send '"+"fps: {}".format(fps)+"'")
    
    #cv2.waitKey(1)
