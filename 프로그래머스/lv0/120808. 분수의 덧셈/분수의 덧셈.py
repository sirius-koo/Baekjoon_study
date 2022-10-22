import fractions

def solution(denum1, num1, denum2, num2):
    answer = []
    
    top = (denum1 * num2) + (denum2 * num1)
    bot = num1 * num2
    a = fractions.Fraction(top, bot)
    answer.append(a.numerator)
    answer.append(a.denominator)
    return answer