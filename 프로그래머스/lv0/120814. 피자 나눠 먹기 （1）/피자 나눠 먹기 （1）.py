def solution(n):
    if 1 <= n <= 7:
        return 1
    elif n % 7 == 0:
        return n // 7
    elif 7 < n <= 100:
        return n // 7 + 1
    