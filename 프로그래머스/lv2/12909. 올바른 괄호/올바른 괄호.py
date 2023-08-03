def solution(s):
    stack = []

    if s[0] == ")":
        return False

    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            out = stack.pop()
            if out == ")":
                return False

    if stack:
        return False
    else:
        return True