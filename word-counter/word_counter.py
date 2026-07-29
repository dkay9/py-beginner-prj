#get user input and store in a variable
text = input("Enter some text: ")

#get the length of the user input
char_count = len(text)
print(f"Character Count: {char_count}")

#split the user input which would turn it into a list and get the length of the list
words = text.split()
word_count = len(words)
print(f"Word count: {word_count}")

#create an empty dictionary
word_freq = {}

#find most frequent word using for loop and an if statement
for word in words:
    word_lower = word.lower()
    if word_lower in word_freq:
        word_freq[word_lower] += 1
    else:
        word_freq[word_lower] = 1

#find the word with the highest count
most_common = max(word_freq, key=word_freq.get)
print(f"Most frequent word: '{most_common}' ({word_freq[most_common]} times)")