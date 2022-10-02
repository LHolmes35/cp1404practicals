"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

When the numerator or denominator aren't considered a valid integer

2. When will a ZeroDivisionError occur?

When the denominator is equal to 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Perhaps by implementing a while loop, to repeat until numerator and denominator takes a value that isn't
equal to or below 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
