num = list(map(int, input().split()))

asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = asc[:]
des.sort(reverse=True)

if num == asc:
    print('ascending')
elif num == des:
    print('descending')
else:
    print('mixed')