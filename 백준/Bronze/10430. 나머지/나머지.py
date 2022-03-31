#map() 함수를 이용한 풀이방법
A, B, C = map(int, input().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

'''
다른 풀이
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
'''
