#!/bin/sh

bash /home/pi/Desktop/psp.sh &
python3 /home/pi/Desktop/buttons.py &

while true; do
  nohup python3 /home/pi/Desktop/display.py
done &
