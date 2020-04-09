import re
import sys
import time
from cryptography.fernet import Fernet

class player:
    lvl=0
    inventory=[]
    
    def show_inventory(self):
        if len(self.inventory) == 0:
            display("You have nothing in your inventory")
        else:
            print("You have :\n")
            for item in self.inventory:
                print("\t",item)
def get_text(keyword,level_text):
    keyword=modify_input(keyword)
    pattern=re.compile(rf'#{re.escape(keyword)}+\s([0-9a-zA-Z\s\'\.,]*)%')
    match=pattern.findall(level_text)
    if match:
        return match[0]
    else:
        return "Error"

def display(strin):
    for l in strin:
        sys.stdout.write(l)
        sys.stdout.flush()
#        time.sleep(0.02)
    print('\n')

def modify_input(keyword):
    if keyword.split()[0] == 'l':
        keyword = keyword.replace('l','look')
    keyword = keyword.replace('examine','x')
    keyword = keyword.replace(' ','+')
    return keyword

def open_room(lvl):
    path="rooms/" + str(lvl) + ".txt"
    with open(path) as f:
        return f.read()

def main():
    key = b'BB05kF8Pc4yLYfLB6Kn-jorUtg1_2ZbDeN70IjXjATA='
    character = player()
    userInput = ""
    level_text = open_room(character.lvl)
    print()
    display(get_text("look",level_text))
    keywords = ['l','look','take','x','examine','go','go','follow','inventory']
    while userInput != "exit":
        userInput=input("> ")
        text = get_text(userInput,level_text)
        if userInput.split(' ')[0] not in keywords:
            display("Come again?")
        elif userInput == "inventory":
            character.show_inventory()
        elif text.isnumeric():
            character.lvl = int(text)
            level_text=open_room(character.lvl)
            userInput="look"
            text = get_text(userInput,level_text)
            display(text)
        elif re.match(r'take \w*$',userInput): 
            if get_text(userInput,level_text) == userInput.split(' ')[1]: 
                character.inventory.append(text)
                display("You took the " + userInput.split(' ')[1] + " !")
            else:
                display("I can't see such a thing!")
        else:
            display(text)
            

main()
