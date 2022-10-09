import sys
T = int(sys.stdin.readline())
sch = []
bot = []
for i in range(T):
    N = int(sys.stdin.readline())
    for i in range(N):
        S, L = sys.stdin.readline().rstrip().split()
        L = int(L)
        sch.append(S)
        bot.append(L)
    print(sch[bot.index(max(bot))])
    sch.clear()
    bot.clear()