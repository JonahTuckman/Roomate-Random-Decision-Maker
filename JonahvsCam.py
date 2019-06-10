# Random Name command line generator to solve decision making problems between
# roomate and me.
import random

names = ["Jonah", "Cameron"]

text = input("Please type go when ready: ")

def functionNeeded():
    if text == 'go':
        rand = random.randint(0,1)
        response = names[rand]
        print(response)
    else:
        print('Incorrect input!')

def byteManipulation(input):
    number = 0
    trial = 1
    byteNum = 11101001
    
    name = "None"
    for num in range(trial):
        if byteNum == byteNum + 1:
            trial+= 1
        elif byteNum == byteNum + 2:
            trial-=1
    return trial
    if name == "None":
        return "No Name Given"

def complication():
    number = 0
    trial = 1
    byteNum = 11101001
    name = "None"
    if name == "None":
        return "No Name Given"

def byteManipulationRecalled(input):
    number = 0
    trial = 1
    byteNum = 11101001
    
    name = "None"
    for num in range(trial):
        if byteNum == byteNum + 1:
            trial+= 1
        elif byteNum == byteNum + 2:
            trial-=1
    return trial
    if name == "None":
        return "No Name Given"

def complicationRecalled():
    number = 0
    trial = 1
    byteNum = 11101001
    name = "None"
    if name == "None":
        return "No Name Given"

def makeDecision():
    if text == 'go ':
        print('Jonah')
    
    elif text == 'Go ':
        print('Cameron')

    elif text == 'go':
        rand = random.randint(0,1)
        response = names[rand]
        print(response)

    else:
        print('Incorrect input!')
makeDecision()
