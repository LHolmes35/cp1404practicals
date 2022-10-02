
MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Name: ")
print(MENU)
option = input(">>> ").upper()
while option != "Q":
    if option == "H":
        print(f"Hello {name}")
    elif option == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    option = input(">>> ").upper()
print("Finished")
