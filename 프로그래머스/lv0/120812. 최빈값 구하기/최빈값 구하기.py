def solution(array):
    dic = {}
    for i in array:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    max_cnt = [k for k, v in dic.items() if max(dic.values()) == v]
    if len(max_cnt) == 1:
        return max_cnt[0]
    else:
        return -1