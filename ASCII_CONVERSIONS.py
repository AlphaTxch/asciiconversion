import random

FirstWord=str(input("Input your word"))
SecondWord=str(input("Input your second word"))

Password= FirstWord.lower() + SecondWord.lower()

for letter in Password:
   
    if letter == "a" or "j" or "o" or "s" or SecondWord:
        replacement = random.randint(33,37)
        print(replacement)
        if letter == "b" or "d" or "e" or FirstWord:
            replacement = random.randint(38,42)
            print(replacement)