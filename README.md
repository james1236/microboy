# microboy
My raspberry pi zero powered mini computer (3d print files, code, product lists)

<img src="photo.png" width="350"></img>
<br>

### Parts
Joystick - Sparkfun COM-09426

Display - 1.3" 240x240 LCD TFT SPI Display (ST7789 Driver) no chip select pin (GND,VCC,SCL,SDA,RES,DC,BLK)

Analog to Digital converter - Adafruit ADS1015 12-bit I2C

Battery - LP603450 LiPoly 3.7V 1000mAh TG15

Battery Charge / Voltage regulator / Transformer board - Adafruit PowerBoost 500 Charger TPS61090 DC Boost (Not strong enough to power pi4 or CM4)

Small Dip Switch (unknown)

9 Momentary Tactile PCB Push Buttons 6mm x 6mm

Raspberry Pi Zero W

<br>

### Wiring
<pre>
RPi BOARD Pin #1 (3.3V) -> Display VCC
       		        -> Joystick VCC (Pin 4)
                        -> ADS1015 VCC

RPi BOARD Pin #2 (5V)  -> PowerBoost 5V

RPi BOARD Pin #6 (GND) -> Display GND
                       -> Joystick GND (Pin 2)
		       -> ADS1015 GND
		       -> PowerBoost GND
                       -> Small Switch Right
                       -> Button 1 Right
                       -> Button 2 Right
                       -> Button 3 Right
                       -> Button 4 Right
                       -> Button 5 Right
                       -> Button 6 Right
                       -> Button 7 Right
                       -> Button 8 Right
                       -> Button 9 Right


RPi BOARD Pin #3 (SDA) -> ADS1015 SDA
RPi BOARD Pin #5 (SCL) -> ADS1015 SCL


RPi BOARD Pin #23 (SCLK) -> Display SCL
RPi BOARD Pin #19 (MOSI) -> Display SDA
RPi BOARD Pin #15 -> Display RES
RPi BOARD Pin #11 -> Display DC
Rpi BOARD Pin #13 -> Display BLK


RPi BOARD Pin #36 -> Button 1 Left
RPi BOARD Pin #22 -> Button 2 Left
RPi BOARD Pin #18 -> Button 3 Left
RPi BOARD Pin #16 -> Button 4 Left
RPi BOARD Pin #37 -> Button 5 Left
RPi BOARD Pin #29 -> Button 6 Left
RPi BOARD Pin #31 -> Button 7 Left
RPi BOARD Pin #40 (PCM_DOUT) -> Button 8 Left
RPi BOARD Pin #38 (PCM_DIN) -> Button 9 Left

ADS1015 A0 -> Joystick X/Y (Pin 1)
ADS1015 A1 -> Joystick X/Y (Pin 3)

PowerBoost EN -> Small Switch Left
</pre>

<br>

### Software

**Run in the console of your raspberry pi:**

```
sudo apt-get install cmake
cd ~
git clone https://github.com/juj/fbcp-ili9341.git
cd fbcp-ili9341
```

Then run `sudo nano display.h` and paste in 

`#define DISPLAY_SPI_DRIVE_SETTINGS (1 | BCM2835_SPI0_CS_CPOL | BCM2835_SPI0_CS_CPHA)`

under the line

`#define DISPLAY_SPI_DRIVE_SETTINGS (0)`

Then continue with

```
mkdir build
cd build
```

Then make sure the SPI interface is turned off either in raspi-config or through `sudo nano /boot/config.txt` and making sure the line `dtparam=spi=off` is there (not sure if this is a necessary step)

If you have previously run 'cmake' and would like a fresh start do this:

```
cd fbcp-ili9341/build
rm -r *
```

Then run the command below changing your wire numbers (if you're using different wiring) for `-DGPIO_TFT_DATA_CONTROL=17 -DGPIO_TFT_RESET_PIN=22 -DGPIO_TFT_BACKLIGHT=27` to the BCM pins from this site https://pinout.xyz/pinout/pin13_gpio27

`cmake -DST7789VW=ON -DGPIO_TFT_DATA_CONTROL=17 -DGPIO_TFT_RESET_PIN=22 -DGPIO_TFT_BACKLIGHT=27 -DSTATISTICS=0 -DSPI_BUS_CLOCK_DIVISOR=40 -DUSE_DMA_TRANSFERS=OFF -DDISPLAY_ROTATE_180_DEGREES=ON ..`

The DMA transfers argument increases the framerate and decreases CPU usage, should be used when possible (disabled because it didn't work for me)
`DSPI_BUS_CLOCK_DIVISOR` should be a minimal even number (start out at something safe like 40, then decrease for better FPS until you notice glitches)

Finally run

```
make -j
sudo ./fbcp-ili9341
```

And if your display is like mine (advertised as ST7789 but ended up working with ST7789VW, no cs pin) it might work

For autorun on startup put this line before `exit 0` in your `sudo nano /etc/rc.local`

`sudo /home/pi/fbcp-ili9341/build/fbcp-ili9341 &`

These lines are in my `sudo nano /boot/config.txt` file:

```
hdmi_group=2
hdmi_mode=87
hdmi_cvt=640 640 60 1 0 0 0
hdmi_force_hotplug=1
```
Make sure that all references to `dtoverlay=vc4-fkms-v3d` are removed/commented out with `#` although I'm not sure if necessary

### 64 bit fbcp-ili9341
To get fbcp-ili9341 working on a rpi 4 running a 64 bit operating system, you can replace the relevant steps above with the following
```
git clone --branch rpi2w-64bit-port https://github.com/zxfishhack/fbcp-ili9341.git
```
(uses a fork of `fbcp-ili9341` with 64 bit compatability)
```
cmake -DST7789VW=ON -DGPIO_TFT_DATA_CONTROL=17 -DGPIO_TFT_RESET_PIN=22 -DGPIO_TFT_BACKLIGHT=27 -DSTATISTICS=0 -DSPI_BUS_CLOCK_DIVISOR=6 -DUSE_DMA_TRANSFERS=ON -DDISPLAY_ROTATE_180_DEGREES=ON -DAARCH64=YES ..
```
Note the difference of `-DUSE_DMA_TRANSFERS=ON`, `-DAARCH64=YES` and `-DSPI_BUS_CLOCK_DIVISOR=6`. DMA transfers increases the framerate and decreases CPU usage, should be used when possible. The DAARCH64 parameter enables some of the changes in the `rpi2w-64bit-port` branch of [zxfishhack's fork](https://github.com/zxfishhack/fbcp-ili9341/tree/rpi2w-64bit-port) of `fbcp-ili9341`. `DSPI_BUS_CLOCK_DIVISOR` should be a minimal even number (start out at something safe like 40, then decrease for better FPS until you notice glitches)

<br>

### Extra info
* Avoid using this display, there is very little compatability for the version of the 240x240 small ST7789 display without a CS pin.
* ~~`fbcp-ili9341` doesn't work on 64 bit operating systems yet~~
* `fbcp-ili9341` puts the screen to sleep after a while of keyboard inactivity, give a keyboard input after starting it if you are getting a black screen
* The ADC python library is depreciated and the wrong version gets installed if you use pip, you can clone it [here](https://github.com/adafruit/Adafruit_Python_ADS1x15), usage guide [here](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115)
* The crontab syntax for starting `fbcp-ili9341` on boot is putting `@reboot root /home/pi/fbcp-ili9341/build/fbcp-ili9341` in `/etc/crontab`
* Neither the Adafruit PowerBoost 500, nor a lipo battery of this size are strong enough to power a RPi 4 or CM4
* On some operating systems, `fbcp-ili9341` won't build and will give the error `selected processor lacks an FPU` unless you remove the flags `-mfloat-abi=hard` and `-mhard-float` from somewhere in `display.h`
* The original Pi Zero W (used here) is too slow for decent internet browsing
* `pyautogui`'s mouse movement is too slow on the Pi Zero W and causes noticeable stutter, use `mouse` instead
