sentence = input("Put a sentence: ")
letter = input("What letter do you want do and the loop with?: ")

for character in sentence :
    if character.lower() == letter.lower():
        break
    elif character.lower() == "a":
        continue
    elif character.lower() == "e":
        continue
    elif character.lower() == "i":
        continue
    elif character.lower() == "o":
        continue
    elif character.lower() == "u":
        continue
    print(character,end="")