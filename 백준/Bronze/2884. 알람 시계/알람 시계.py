H, M = map(int, input().split())
set_h, set_m = 0, 0
if ((M-45) > 0):
    set_h = H
    print(set_h, M-45)
elif ((M-45) < 0):
    set_h = H -1
    if set_h < 0:
        set_h = 23
    set_m = M + 15
    print(set_h, set_m)
elif ((M-45) == 0):
    set_h = H
    set_m = M - 45
    print(set_h, set_m)