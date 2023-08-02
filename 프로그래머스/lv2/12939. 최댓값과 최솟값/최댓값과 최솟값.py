def solution(s):
    num_list = s.split(' ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    max_num = str(max(num_list))
    min_num = str(min(num_list))
    return min_num + ' ' + max_num
    