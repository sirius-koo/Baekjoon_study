w = list(input())
cnt = {}
max_cnt = []
w_string = ''.join(str(n) for n in w)
W_string = w_string.upper()
W_list = list(W_string)
W_listset = list(set(W_string))
for i in W_string:
    try:
        cnt[i] += 1
    except:
        cnt[i] = 1

max_cnt = [k for k, v in cnt.items() if max(cnt.values()) == v]
if len(max_cnt) == 1:
    print(max_cnt[0])
else:
    print("?")