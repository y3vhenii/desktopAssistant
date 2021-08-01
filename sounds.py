import chime
import time 

# Used to let the user know that he is being listed to.
def imListening():
    chime.info()
    time.sleep(0.5)

# Notifies the user about completion of the process.
def timeIsUp():
    chime.success()
    time.sleep(0.5)
    chime.success()
    time.sleep(0.5)
    chime.success()

# Error sound
def playErr():
    chime.warning()