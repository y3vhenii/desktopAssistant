import pyttsx3

# Provides list of commands to the user
def commandList():
    f = open("commands.txt", "r")
    print(f.read())
    
# Adds new command to the list
def addNewCommand():
    engine = pyttsx3.init()
    engine.say("Which command would you like to add?")
    engine.runAndWait()
    command = input("New command: ").lower()
    f = open("commands.txt", "a")
    f.write(command + "\n")
    f.close()
    engine.say("Done")
    engine.runAndWait()
    engine.stop()

# Standard commands (add, remove commands)
def delCommand():
    engine = pyttsx3.init()
    engine.say("Which command would you like to remove?")
    engine.runAndWait()
    commandToDelete = input("Command to delete: ").lower()
    with open("commands.txt", "r") as f:
        lines = f.readlines()
    with open("commands.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != commandToDelete:
                f.write(line)
    engine.say("Done")
    engine.runAndWait()
    engine.stop()