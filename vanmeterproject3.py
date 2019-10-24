source = open('modest.txt')

modest = source.read()



import re

def book(words):
    if type(words) != str:
        raise TypeError ("Not A String")

    result = re.findall('\\w+at\\b', words)
        
