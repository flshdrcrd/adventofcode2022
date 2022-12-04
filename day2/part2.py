solution = 0
f = open("day2/input.txt", "r")
while True:
    line = f.readline()
    if line == "":
        break
    round = line
    decode = {"A":"rock", "B":"paper", "C":"scissors"}
    opponent = decode[round[0]]
    decode = {"X":"lose", "Y":"draw", "Z":"win"}
    outcome = decode[round[2]]

    if outcome == "lose" and opponent == "paper" or outcome == "draw" and opponent == "rock" or outcome == "win" and opponent == "scissors":
        you = "rock"

    if outcome == "lose" and opponent == "scissors" or outcome == "draw" and opponent == "paper" or outcome == "win" and opponent == "rock":
        you = "paper"

    if outcome == "lose" and opponent == "rock" or outcome == "draw" and opponent == "scissors" or outcome == "win" and opponent == "paper":
        you = "scissors"

    score = 0
    if you == "rock":
        score += 1
    elif you == "paper":
        score += 2
    elif you == "scissors":
        score += 3
    if opponent == "rock" and you == "paper" or opponent == "paper" and you == "scissors" or opponent == "scissors" and you == "rock":
        score += 6
    elif opponent == "rock" and you == "rock" or opponent == "paper" and you == "paper" or opponent == "scissors" and you == "scissors":
        score += 3
    solution += score
print(solution)