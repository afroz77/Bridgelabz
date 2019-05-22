import random
stake = int(input("Enter Stake : "))

while stake <= 0:
    stake = int(input("Stake Should Be Greater Than 0 : "))

goal=int(input("Enter Goal : "))
while stake >= goal:
    goal = int(input("Goal Should Be Greater Than Stake : "))
Iteration = int(input("Enter Trials : "))
cash = stake
wn = ls = wp = lp = bet = 0
for i in range(Iteration):
        if cash == goal:
            break
        if cash > 0:
            x = random.randint(0, 1)
            if x == 1:
                cash += 1
                wn += 1
                bet += 1
            else:
                cash -= 1
                ls += 1
                bet += 1
try:
    wp = (wn/bet)*100
    lp = (ls/bet)*100
except:
    print("Divide By Zero Error")

if wn > ls or cash == goal:
    print("\nYou Win")
elif wn == ls:
    print("\nMatch Tied")
else:
    print("\nYou Lose")

print("\nYou Played ", bet, " Bets")
print("You Wins ", wn, " Times")
print("You Lose ", ls, " Times")
print("Win Percentage Is ", round(wp, 2))
print("Lose Percentage Is ", round(lp, 2))
print("Total Cash", cash)
