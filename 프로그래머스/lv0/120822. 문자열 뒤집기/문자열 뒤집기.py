def solution(my_string):
    li_ = list(my_string)
    return ''.join(k for k in li_[::-1])

# 간결한 방법이 있었다..
def solution(my_string):
    return my_string[::-1]
