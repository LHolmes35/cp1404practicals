"""
CP1404 Practical
Unreliable Car Test program
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    new_car = UnreliableCar("Kia Cerato 5", 100, 90)
    old_car = UnreliableCar("Hyundai Coupe SX", 100, 7)

    print(f"Let try driving:")
    print(f"{new_car.name} drove {new_car.drive(50)} km")
    print(f"{old_car.name} drove {old_car.drive(50)} km")


main()
