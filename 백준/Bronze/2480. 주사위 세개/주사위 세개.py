import sys

prize = 0
dice = list(sys.stdin.readline().rstrip().split())

if (dice[0] != dice[1] and dice[0] != dice[2] and dice[1] != dice[2]):
    prize = int(max(dice)) * 100
elif (dice[0] == dice[1] == dice[2]):
    prize = 10000 + int(dice[0]) * 1000
elif (dice[0] == dice[1]):
    prize = 1000 + int(dice[0]) * 100
elif (dice[1] == dice[2]):
    prize = 1000 + int(dice[1]) * 100
elif (dice[0] == dice[2]):
    prize = 1000 + int(dice[0]) * 100
print(prize)