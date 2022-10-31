# 내 학점을 구해줘
import sys

T = int(sys.stdin.readline())
c_, v_ = [], []
for i in range(T):
    c, v = map(int, sys.stdin.readline().split())
    c_.append(c)
    v_.append(v)
for i in range(T):
    print("You get {} piece(s) and your dad gets {} piece(s).".format(c_[i] // v_[i], c_[i] - (c_[i] // v_[i]) * v_[i]))
