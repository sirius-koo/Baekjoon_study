def solution(s):
    a, b = 0, 1
    for i in range(s):
        a, b = b, a + b
    return a % 1234567