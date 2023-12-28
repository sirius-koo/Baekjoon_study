def solution(n):
    tmp = []
    for i in range(1, n):
        if n % i == 1:
            tmp.append(i)

    return min(tmp)