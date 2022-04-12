#BOJ_11653
N = int(input())
i = 2
while N >= 2:
    if N % i == 0:
        print(i)
        N = N / i
    else:
        i += 1
'''
입력-정수 N
출력-N의 소인수분해 결과를 한 줄에 하나씬 오름차순으로 N이 1인 경우 아무것도 출력x
소인수분해 이므로 i는 1부터가 아닌 2부터 시작해야 함. 계속 분해해야 하므로 N을 i로 나눈 값을 N에 대입!
https://needneo.tistory.com/112
'''
