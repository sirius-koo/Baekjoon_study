def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    
    num = list(map(str, numbers))
    num.sort(key=lambda x:x*3, reverse=True)
    return ''.join(num)