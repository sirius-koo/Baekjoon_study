n = int(input())

def factorial(n):
    output = 1
    
    for i in range(1, n + 1):
        output *= i
    
    return output

print(factorial(n))