import json   # importing libraries
from difflib import get_close_matches


data = json.load(open("data.json"))   ##loading python into data type

def translate(w):  # need 3 conditionals
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()] # print Texas instead of texas
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "This word does not exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "This word does not exist. Please double check it."

word = input("Enter a Word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
