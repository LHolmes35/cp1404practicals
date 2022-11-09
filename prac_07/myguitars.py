"""
CP1404 - My guitars program
Prac 07
"""

from prac_06.guitar import Guitar


def main():
    """Display guitars using Guitar class"""
    guitars = get_guitars()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_guitars():
    """Get guitars from guitars csv file"""
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        parts[1] = int(parts[1])
        parts[2] = float(parts[2])
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
