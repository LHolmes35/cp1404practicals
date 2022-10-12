
import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    amount_of_picks = int(input("How many quick picks? "))
    while amount_of_picks < 0:
        print("Invalid number")
        amount_of_picks = int(input("How many quick picks? "))

    for i in range(amount_of_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
