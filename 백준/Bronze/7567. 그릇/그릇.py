import sys

cnt = 10
list_b = list(sys.stdin.readline().rstrip())
for i in range(1, len(list_b)):
    if list_b[i-1] == '(':
        if list_b[i] == '(':
            cnt += 5
        elif list_b[i] == ')':
            cnt += 10
    elif list_b[i-1] == ')':
        if list_b[i] == ')':
            cnt += 5
        elif list_b[i] == '(':
            cnt += 10
print(cnt)