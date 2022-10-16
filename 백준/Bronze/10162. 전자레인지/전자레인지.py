import sys

T = int(sys.stdin.readline())
A, B, C = 300, 60, 10
cnta, cntb, cntc = 0, 0, 0

while True:
    T -= A
    cnta += 1
    if T < 0:
        cnta -= 1
        T += A
        break
while True:
    T -= B
    cntb += 1
    if T < 0:
        cntb -= 1
        T += B
        break
while True:
    T -= C
    cntc += 1
    if T < 0:
        cntc -= 1
        T += C
        break
if T != 0:
    print(-1)
else:
    print(cnta, cntb, cntc)