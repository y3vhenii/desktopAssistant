import pyttsx3
import webbrowser

# Provides list of commands to the user
def commandList():
    print(" ")
    print("*****************************")
    print("*** ALL POSSIBLE COMMANDS ***")
    print("*****************************")
    f = open("commands.txt", "r")
    print(f.read())
    print("*****************************")
    
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

# Remove command from the list
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

#Ask a question
def askQuestion():
    engine = pyttsx3.init()
    engine.say("Whats your question?")
    engine.runAndWait()
    question = input("Question: ").lower()  
    engine.say("Since I am not an AI yet, I can't come up with the answer myself, but I will Google it for you.")
    engine.runAndWait()
    question = question.replace(' ', '%20')
    webbrowser.open("http://www.google.com/search?q=" + question, new=1)
