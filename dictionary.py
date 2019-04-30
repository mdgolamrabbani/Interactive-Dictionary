# import json library
import json
#Import library which will find similarity ratio between two wrods
from difflib import get_close_matches

# load json data
data = json.load(open("data.json"))

#Create a function that will return the meaning of the word which is entered by user
#If the word does not exist then it will show a message

def translate(word):
    word = word.lower()#if the use enter word with mix lower and upper case letter then it will convert the data with lowercase
    if word in data:
        return data[word]
    elif word.title() in data:# this will make the first letter in Uppercase
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(word, data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn=="N":
            return "The word does't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exist, please double check it."

#Ask a user to enter a word
word = input("Enter word: ")

#Now call the function to print the output

output = translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
