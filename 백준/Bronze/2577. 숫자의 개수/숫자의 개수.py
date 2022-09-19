A = input()
B = input()
C = input()
axbxcx = str(int(A) * int(B) * int(C))
list_abc_str = list(axbxcx)
list_abc_int = [int(i) for i in list_abc_str]
print(list_abc_int.count(0))
for i in range(1, 9 + 1):
    print(list_abc_int.count(i))