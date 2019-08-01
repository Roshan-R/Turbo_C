import msvcrt
import time
import sys

def modify(ch,val):
    ch = ch.replace('examine','x')
    if ch.split()[0] == 'l':
        ch = ch.replace('l','look')
    ch = ch.replace(' ','+')
    ch = ch + val
    return ch

def get_lines(inp,f):
    passage = f.read().split('%')
    for x in passage:
        if inp in x.split():
            f.seek(0)
            return x.replace(inp, '').lstrip()

def display(strin):
    for l in strin:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)
    print('\n')


keywords = ['intro','l','look','exit','examine','x','go']
ch = 'look'
val = '0'
f = open("story.txt","r")
fs = f.read()
f.seek(0)
display(get_lines(ch + val,f))
while ch != "exit":
    if msvcrt.kbhit():
        key = msvcrt.getch()
        print(key)
    ch = input("> ")
    chr = modify(ch,val)
    if ch.split()[0] not in keywords :
        print("That is not a verb I recognize")
    elif chr not in fs:
        print("You can't see any such thing.")
    elif ch.split()[0] == "go":
        val = get_lines(chr,f)
        print(get_lines("look" + val,f))
    else:
        display(get_lines(chr,f))

