# TODO: Add if statements

import os, sys, random
import time
from datetime import datetime

#the print function
def yap(message):
    print(message)
#create a variable
def memorize(variable , value):
    variable
    value
    variable = value
#recite the variable
def recite(variable):
    try:
        yap(variable)
    except:
        yap("fuck no")

def what(message):
    input(message)
def rand(max):
    try:
        max = random.randint(0, int(max))
        error = False
    except:
        print("bro WTF")
        error = True
    if error == False:
        print(max)
def time():
    now = datetime.now()
    print(now)
def yap_endlessly():
    ya = random.randint(0, 50)
    for i in range(ya):
        print("gaysam!")
    error = False
        
    
    
os.system('clear')
print("Welcome to cheetoscript!\nVersion 0.2\nType \"help()\" if you cant comprehend this!")

while True:
    error = True
    token = input('> ')

    # Real commands #####################

    # yap command (doesn't require quotes)
    if token.startswith("yap("):
        try:
            string = token.replace("yap(", "", 1)
            string = string.replace(")", "", 1)
            yap(string)
            error = False
        except:
            error = True
    #ask the user something
    if token.startswith("what("):
        try:
            string = token.replace("what(", "", 1)
            string = string.replace(")", "", 1)
            what(string)
            error = False
        except:
            error == True
    # Output a variable
    if token.startswith("recite("):
        try:
            try:
                x = token.replace("recite(", "", 1)
                x = x.replace(")", "", 1)
                recite(value)
            except:
                print(variable)
            error = False
        except:
            print("schizofrenia ass, this variable dont exist!")
            error = True

    # Variable assignment (Only 1 variable at a time)
    if token.startswith("memorize("):
        try:
            x = token.replace("memorize(", "", 1)
            x = x.replace("memorize(", "", 1)
            x = x.replace(")", "", 1)
            temp = x
            x = x.replace(", ", "", 1)

            original = temp
            index = original.find(", ") + 2
            value = original[index:]
            var = original[:index - 2]
            memorize(var , value)
            error = False
        except:
            error = True
    if token.startswith('rand('):
        try:

            x = token.replace("rand(", "", 1)
            x = x.replace(")", "", 1)
            rand(x)

            error = False
        except:
            error = True

    #simple functions
    if token == 'yap_endlessly()':
        yap_endlessly()   

    #print time
    if token == 'time()':
        time()
        error = False
    #get help(something i need)
    if token == 'help()':
        try:
            import other.help
            error = False
        except:
            error = True
            #exit
    if token == 'exit()':
        #yap("ok, bye fucko!")
        sys.exit()
    #clear the log
    if token == 'cls' or token == 'clear':
        os.system('clear')
        error = False
    # End ###############################    
    if error == True:
        print("useless piece of shit! try again!")