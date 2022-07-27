#code wars Kata link: https://www.codewars.com/kata/5842df8ccbd22792a4000245
def expanded_form (num):

    num_exp = list(reversed(str(num)))

    exp_new = []

    for i in range (len(num_exp)):
        calc = int(num_exp[i]) * (10**i)

        if calc > 0:
            exp_new.append(str(calc))

    txto = ' + '.join(reversed(exp_new))

    return txto


print (expanded_form(70304))