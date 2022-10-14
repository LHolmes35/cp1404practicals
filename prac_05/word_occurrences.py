"""
Word Occurrences
Estimate: 25 minutes
Actual:
"""

word_to_amount = {}

text = input("Text: ")
words = text.split()
for word in words:
    amount = word_to_amount.get(word, 0)
    word_to_amount[word] = amount + 1


