C1, C2 = list(map(str, input().split()))
C1list, C2list = list(C1), list(C2)
C1list_re, C2list_re = list(reversed(C1list)), list(reversed(C2list))
c1 = int(''.join(str(n) for n in C1list_re))
c2 = int(''.join(str(n) for n in C2list_re))
if c1 > c2:
    print(c1)
elif c1 < c2:
    print(c2)