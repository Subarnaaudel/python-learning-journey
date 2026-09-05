# wap to print the content of a directory using th eos module. search online for the function which does that
import os

path = "D:/chapter_1"

contents = os.listdir(path)

for item in contents:
    print(item)