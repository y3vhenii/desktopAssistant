import pyttsx3
from basicCommands import *

# Initializing assistant
engine = pyttsx3.init()
engine.say("Welcome to desktop assistant. Here is the list of commands that I recognize: ")
engine.runAndWait()
commandList()
terminate = False
while terminate == False:
    engine.say("I'm waiting for your command...")
    engine.runAndWait()
    command = input("Command: ").lower()
    if command == "add new command":
        addNewCommand()
    elif command == "remove command":
        delCommand()
    elif command == "exit":
        terminate = True
        engine.stop()
    elif command == "list all possible commands":
        engine.say("Here are all the commands I know so far: ")
        engine.runAndWait()
        commandList()
    else:
        engine.say("I don't recognize this command. Sorry!")
        engine.runAndWait()