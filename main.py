import random

old_string = "The Broncos just made the playoffs for the first time in nine years"

def new_string(string):
    result = ""
    for i, character in enumerate(string):
        if i % 2 == 0:
             result += character.upper()
        else:
            result += character.lower()
    return result

print(new_string(old_string))