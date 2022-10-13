import sys

N = int(sys.stdin.readline())
abc = []
abc_cal = []

def dice_cal(x, y, z):
    xyz = [x, y, z]
    if (x != y and x != z and y != z):
        return (max(xyz) * 100)
    elif (x == y == z):
        return (10000 + (x * 1000))
    elif (x == y):
        return (1000 + (x * 100))
    elif (x == z):
        return (1000 + (x * 100))
    elif (y == z):
        return (1000 + (y * 100))

for i in range(N):
    a = list(sys.stdin.readline().rstrip().split())
    abc.append(list(a))
    abc_cal.append(dice_cal(int(abc[i][0]), int(abc[i][1]), int(abc[i][2])))
print(max(abc_cal))