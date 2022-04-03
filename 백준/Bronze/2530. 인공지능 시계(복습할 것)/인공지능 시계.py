h, m, s = map(int, input().split())
timer = int(input())

s += timer % 60
timer = timer // 60
if s >= 60:
    m += 1
    s -= 60
m += timer % 60
timer = timer // 60
if m >= 60:
    h += 1
    m -= 60
h += timer % 24
if h >= 24:
    h -= 24
print(h, m, s)
