import sys

list_x, list_y = [], []
x_, y_ = 0, 0
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    list_x.append(x)
    list_y.append(y)
if (list_x[0] == list_x[1]):
    x_ = list_x[2]
elif (list_x[1] == list_x[2]):
    x_ = list_x[0]
elif (list_x[0] == list_x[2]):
    x_ = list_x[1]

if (list_y[0] == list_y[1]):
    y_ = list_y[2]
elif (list_y[1] == list_y[2]):
    y_ = list_y[0]
elif (list_y[0] == list_y[2]):
    y_ = list_y[1]

print(x_, y_)