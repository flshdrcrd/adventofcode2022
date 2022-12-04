solution = 0
f = open("day3/input.txt", "r")
while True:
    line = f.readline()
    if line == "":
        break
    rucksack = line
    rs_size = len(rucksack)
    comp_1 = []
    comp_2 = []
    itemno = 0
    for x in rucksack:
        itemno += 1
        if itemno <= rs_size / 2:
            comp_1.append(x)
        else:
            comp_2.append(x)
    for x in comp_1:
        if x in comp_2:
            inboth = x
    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if inboth in abc_lower:
        num = 1
        for x in abc_lower:
            if x == inboth:
                priority = num
            else:
                num += 1
    elif inboth in abc_upper:
        num = 27
        for x in abc_upper:
            if x == inboth:
                priority = num
            else:
                num += 1
    solution += priority
print(solution)