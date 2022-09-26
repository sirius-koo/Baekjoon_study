import sys

w = list(sys.stdin.readline().rstrip())
for i in range(len(w)):
    if w[i].isupper():
        w[i] = w[i].lower()
    else:
        w[i] = w[i].upper()
W = ''.join(str(n) for n in w)
print(W)