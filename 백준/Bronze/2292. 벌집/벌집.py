import sys
N = int(sys.stdin.readline())
cnt = 1 # 시작점
cnt_room = 6 # 지나가야 하는 방의 개수가 6의 배수
cnt_min = 1 
while N > cnt:
    cnt_min += 1 # 최소 개수로 방을 지나가는 방법
    cnt += cnt_room 
    cnt_room += 6
print(cnt_min)
