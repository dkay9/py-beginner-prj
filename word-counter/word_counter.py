text = input("Enter some text: ")

char_count = len(text)
print(f"Character Count: {char_count}")
words = text.split()
word_count = len(words)
print(f"Word count: {word_count}")

word_freq = {}

for word in words:
    word_lower = word.lower()
    if word_lower in word_freq:
        word_freq[word_lower] += 1
    else:
        word_freq[word_lower] = 1

most_common = max(word_freq, key=word_freq.get)
print(f"Most frequent word: '{most_common}' ({word_freq[most_common]} times)")