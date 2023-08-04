def solution(arr):
    answer = []
    temp_value = ""

    for i in range(len(arr)):
        if temp_value != arr[i]:
            answer.append(arr[i])
        elif temp_value == arr[i]:
            continue
        temp_value = arr[i]

    return answer