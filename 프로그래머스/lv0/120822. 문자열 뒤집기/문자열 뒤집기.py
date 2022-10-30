def solution(my_string):
    li_ = list(my_string)
    return ''.join(k for k in li_[::-1])