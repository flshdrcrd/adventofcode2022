solution = 0
a = 0
f = open("day3/input.txt", "r")
while True:
    line = f.readline()
    if line == "":
        break
    if a == 0:
        group = []
        group.append(line)
        a = 1
    elif a == 1:
        group.append(line)
        a = 2
    elif a == 2:
        group.append(line)
        for x in group[0]:
            if x in group[1] and x in group[2]:
                badge = x
                break
        abc_lower = "abcdefghijklmnopqrstuvwxyz"
        abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if badge in abc_lower:
            num = 1
            for x in abc_lower:
                if x == badge:
                    priority = num
                else:
                    num += 1
        elif badge in abc_upper:
            num = 27
            for x in abc_upper:
                if x == badge:
                    priority = num
                else:
                    num += 1
        solution += priority
        a = 0
print(solution)