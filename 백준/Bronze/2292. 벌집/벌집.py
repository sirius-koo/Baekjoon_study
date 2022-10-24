import sys
N = int(sys.stdin.readline())
cnt = 1 # 시작점
cnt_room = 6
cnt_min = 1 
while N > cnt:
    cnt_min += 1
    cnt += cnt_room
    cnt_room += 6
print(cnt_min)