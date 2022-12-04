solution = 0
f = open("day4/input.txt", "r")
while True:
    line = f.readline()
    if line == "":
        break
    line = line.strip()
    pair = line.split(",")
    elf1 = pair[0].split("-")
    elf2 = pair[1].split("-")
    a = int(elf1[0])
    b = int(elf1[1])
    c = int(elf2[0])
    d = int(elf2[1])
    if a <= c and b >= d or a >= c and b <= d:
        solution += 1
print(solution)