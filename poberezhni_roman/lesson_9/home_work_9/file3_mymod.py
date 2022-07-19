import os  #використання цього модулю та функції popen ускладнює життя...
           # хочу подивитись у кого це працює...
           # використав загальну функцию open - вона супер

def count_lines(name: str) -> int:
    a = open(name, 'r')
    b = len(a.readlines())
    return b


def count_chars(name: str) -> int:
    a = open(name, 'r')
    b = len([*a.read()])
    return b

def test(name: str):
    return count_lines(name), count_chars(name), name

file = 'file3_mymod.py'
print(f"Document '{test(file)[2]}'\nLines in document: {test(file)[0]} \nChars in document: {test(file)[1]}")