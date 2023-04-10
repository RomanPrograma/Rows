string = input("Enter a string: ")
word = input("Enter a word: ")
count = 0
for i in range(len(string)):
    if string[i:i+len(word)] == word:
        count += 1
print("The word", word, "occurs", count, "times in the string", string)