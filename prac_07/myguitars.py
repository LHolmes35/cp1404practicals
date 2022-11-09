"""
CP1404 - My guitars program
Prac 07
"""

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Display guitars using Guitar class, add and export new guitars"""
    guitars = get_guitars()
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    print("Lets add to your collections")
    new_name = input("Name: ")
    while new_name != "":
        new_year = int(input("Year: "))
        new_cost = float(input("Cost: $"))
        guitar_to_add = Guitar(new_name, new_year, new_cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        new_name = input("Name: ")
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year}, {guitar.cost}", file=out_file)
    print("Good choices, the collection looks good")


def get_guitars():
    """Get guitars from guitars csv file"""
    guitars = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        parts[1] = int(parts[1])
        parts[2] = float(parts[2])
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
