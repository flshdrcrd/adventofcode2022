f = open("day1/input.txt", "r")
inventory = 0
emptyline = 0
all_inventory = []
while True:
    line = f.readline()
    if line == "":
        all_inventory.append(inventory)
        inventory = 0
        break
    if line == "\n":
        all_inventory.append(inventory)
        inventory = 0
    else:
        inventory += int(line)
all_inventory.sort(reverse=True)
print(all_inventory[0] + all_inventory[1] + all_inventory[2])