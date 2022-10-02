"""
CP1404 - Prac 02 refactoring
"""


def main():
    score = float(input("Enter score: "))
    determine_grade(score)


def determine_grade(score):
    """Determine the result of score"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
