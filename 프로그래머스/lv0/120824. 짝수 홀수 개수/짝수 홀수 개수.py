def solution(num_list):
    odd, even = [], []
    for num in num_list:
        if (num % 2 == 0):
            even.append(num)
        else:
            odd.append(num)
    return [len(even), len(odd)]