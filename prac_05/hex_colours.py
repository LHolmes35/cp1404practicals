
NAME_TO_CODE = {"Candy Pink": "#e4717a", "Denim": "#1560bd", "Magic Mint": "#aaf0d1", "Light": "#eedd82", "Pumpkin": "#ff7518", "Wisteria": "#c9a0dc", "SkyBlue": "#87ceeb", "Mango": "#fdbe02", "Hunter Green": "355e3b", "Carnelian": "b31b1b"}

print(NAME_TO_CODE)
colour_code = input("Select a colour to get it's code: ")
while colour_code != "":
    try:
        print(f"The colour code for {colour_code} is {NAME_TO_CODE[colour_code]}")
    except KeyError:
        print("Invalid colour name")
    colour_code = input("Select a colour to get it's code: ")
