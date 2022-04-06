T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    S = str(S)
    for i in range(len(S)):
        print(R * S[i], end = '')
    print()
    
'''
내가 생각한 코드

T = int(input())
output = []
for i in range(0, T):
    R, S = map(str, input().split())
    output.append(R)
    output.append(S)
for i in range(0, len(output[1])):
    print(output[1][i] * int(R), end = '')
'''
