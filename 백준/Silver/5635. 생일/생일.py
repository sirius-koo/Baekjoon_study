import sys

n = int(sys.stdin.readline())
total = []
for i in range(n):
    student = sys.stdin.readline().rstrip().split()
    student = [str(student[0]), int(student[1]), int(student[2]), int(student[3])]
    total.append(student)
total.sort(key=lambda x: (-x[3], -x[2], -x[1]))
print(total[0][0])
print(total[-1][0])