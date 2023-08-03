def solution(A, B):
    result = 0
    A, B = sorted(A), list(reversed(sorted(B)))
    print(A, B)
    
    for i in range(len(A)):
        result += A[i] * B[i]
    return result