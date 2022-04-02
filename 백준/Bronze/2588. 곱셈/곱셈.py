input_1 = input()
input_2 = input()
#공백없는 문자열 자르기 - list() 함수 이용
input_2_lst = list(input_2)
print(int(input_1) * int(input_2_lst[2]))
print(int(input_1) * int(input_2_lst[1]))
print(int(input_1) * int(input_2_lst[0]))
print(int(input_1) * int(input_2))
