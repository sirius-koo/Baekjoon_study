import sys

n = int(sys.stdin.readline())
Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if (a == 0 and b == 0) or (a == 0 and (b > 0 or b < 0)) or((a < 0 or a > 0) and b ==0):
        AXIS += 1
    elif a > 0 and b > 0:
        Q1 += 1
    elif a < 0 and b > 0:
        Q2 += 1
    elif a < 0 and b < 0:
        Q3 += 1
    elif a > 0 and b < 0:
        Q4 += 1
    
print('Q1:', Q1)
print('Q2:', Q2)
print('Q3:', Q3)
print('Q4:', Q4)
print('AXIS:', AXIS)