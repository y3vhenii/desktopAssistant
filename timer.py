import time
import chime
from sounds import *

# pip3 install chime

# Countdown the minutes
def timer(t):
    t = t*60
    while t:
        minutes, seconds = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(minutes,seconds)
        print(timeformat, end='\r')
        time.sleep(1)
        t -=1 
    # Play the sound
    timeIsUp()

