import sys

dict_ = {
    1: 1,
    2: 1
}
cnt = 0

def fibonacci(n):
    global cnt
    cnt += 1

    if n in dict_:
        return dict_[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dict_[n] = output
        return output

n = int(sys.stdin.readline())
print(fibonacci(n))