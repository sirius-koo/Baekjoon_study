S = list(input())
result = []
for i in range(26):
    if (chr(i+97) in S):
        result.append(S.index(chr(i+97)))
    else:
        result.append(-1)
for i in result:
    print(i, end=" ")