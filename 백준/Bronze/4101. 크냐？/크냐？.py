import sys

a, b = 1, 1

while a != 0 and b != 0:
    a, b = map(int, sys.stdin.readline().split())
    if a != 0:
        if a > b:
            print("Yes")
        else:
            print("No")

'''
*주의해야할 점*

입력의 마지막에 0 0 출력이 아닌
0 0을 입력했을 때 프로그램이 끝나야 함!!
'''
