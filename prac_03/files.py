
out_file = open("name.txt", "w")
name = input("What is your name?: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(f"Total is {total}")
