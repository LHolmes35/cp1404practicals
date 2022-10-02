"""
Randoms questions:

Question 1 - I saw 17, the smallest number can be 5, the largest being 20

Question 2 - I saw 7, the smallest number can be 3, the largest being 10.
    Line 2 can't produce 4, because the range starts at 3, and steps up
    every 2 integers. So it would go 3 then 5, skipping 4.

Question 3 - I saw 3.489030968883733, the smallest number can be 2.5, the
    largest being 5.5
"""

import random

number = random.randint(1, 100)
print(f"Your random number is {number}")
