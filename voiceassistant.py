import pyttsx3
from basicCommands import *
from weather import *
from geoCoder import *
from sendEmail import *

# Initializing assistant
engine = pyttsx3.init()
engine.say("Welcome to Desktop Assistant. Here is the list of commands that I recognize: ")
engine.runAndWait()
commandList()
terminate = False
while terminate == False:
    engine.say("I am waiting for your next command...")
    engine.runAndWait()
    command = input("Command: ").lower()
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
    elif command == "ask a question":
        askQuestion()
    else:
        engine.say("I don't recognize this command. Sorry!")
        engine.runAndWait()