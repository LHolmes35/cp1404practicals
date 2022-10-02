

def main():
    score = int(input("Enter score: "))
    determine_grade(score)
    print_stars(score)


def determine_grade(score):
    """Determine the result of score"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 85:
        print("Excellent")
    elif score >= 75:
        print("Very Good")
    elif score >= 65:
        print("Good")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_stars(score):
    """Printing score in stars"""
    for i in range(score):
        print('*', end='')
    return


main()
