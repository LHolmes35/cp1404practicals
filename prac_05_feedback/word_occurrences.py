"""
Word Occurrences
Estimate: 25 minutes
Actual: 31 minutes
"""

word_to_amount = {}

text = input("Text: ")
words = text.split()
for word in words:
    amount = word_to_amount.get(word, 0)
    word_to_amount[word] = amount + 1

words = list(word_to_amount.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_amount[word]}")
