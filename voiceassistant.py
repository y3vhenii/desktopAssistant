# TODO: Adjust speech recognition to recognize commands even when a few letters don't match.
# TODO: Possibly adjust command recognition even when words or sounds don't match hard-coded commands.
# TODO: Add more functions...

import pyttsx3
from basicCommands import *
from weather import *
from geoCoder import *
from sendEmail import *
from speechRecogn import *
from timer import *
from sounds import *


# Initializing assistant
engine = pyttsx3.init()
engine.say("Welcome to Desktop Assistant. Here is the list of commands that I recognize: ")
engine.runAndWait()
commandList()
terminate = False
while terminate == False:
    engine.say("I'm waiting on your command. Press enter when you're ready...")
    engine.runAndWait()
    input("Press Enter: ")
    # Call speech recognition function (listening time 4 seconds)
    command = recognizeVoice()
    if command == "add new command":
        addNewCommand()
    elif command == "remove command":
        delCommand()
    elif command == "exit":
        terminate = True
        engine.say("Goodbye")
        engine.runAndWait()
        engine.stop()
    elif command == "list all possible commands":
        engine.say("Here are all the commands I know so far: ")
        engine.runAndWait()
        commandList()
    elif command == "get weather update at your location":
        engine.say("Where are you located now?")
        engine.runAndWait()
        location = input("Location: ").lower()
        getMyWeatherUpdate(location)
    elif command == "send email":
        engine.say("Who are you sending the email to?")
        engine.runAndWait()
        recipient = input("Recipient: ").lower()
        subject = input("Subject: ")
        sendEmail(str(recipient), str(subject))
    elif command == "ask question":
        askQuestion()
    elif command == "set timer":
        engine.say("For how many minutes?")
        engine.runAndWait()
        minutes = input("Minutes: ")
        timer(int(minutes))
        time.sleep(1)
    else:
        playErr()
        time.sleep(0.5)
        engine.say("I don't recognize this command. Sorry!")
        engine.runAndWait()