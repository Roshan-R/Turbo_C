import re
import sys
import time
from cryptography.fernet import Fernet

class player:
    lvl=0

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
    level_text = open_room(character.lvl)
    keyword="look"
    while keyword != "exit":
        keyword=input("> ")
        text = get_text(keyword,level_text)
        if text.isnumeric():
            character.lvl = int(text)
            level_text=open_room(character.lvl)
            keyword="look"
            text = get_text(keyword,level_text)
        display(text)
            

main()
