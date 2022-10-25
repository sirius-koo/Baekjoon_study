import sys

odd, even = [], []
for i in range(7):
    num = int(sys.stdin.readline())
    if (num % 2 == 1):
        odd.append(num)
    else:
        even.append(num)
if (odd == []):
    print(-1)
elif (len(odd) >= 1): # len(odd) > 1의 반례 : 홀수가 1개일 때, if (odd == [])에서 홀수가 없을 경우를 제외했으니 '>='를 사용하는게 맞다..
    print(sum(odd))
    print(min(odd))
