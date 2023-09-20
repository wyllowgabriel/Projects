sentence = input("Put a sentence: ")
word = input("Put the word to delete: ")
substring = ""
position = sentence.find(word)
substring = sentence[0:position ]+ sentence[position + len(word) + 1:]
print(substring)

 