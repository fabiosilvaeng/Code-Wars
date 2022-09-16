#code wars Kata link: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
def first_non_repeating_letter(strng):
    minu = strng.lower()
    repet1 = ''

    for i in minu:
        qtd_letra = 0
        letra = i
        for u in minu:
            if letra == u:
                qtd_letra += 1
        if qtd_letra == 1:
            repet1 += letra
    
    if len(repet1) > 0:
        prime = repet1[0]
        for i in range (len(strng)):
            if strng[i].lower() == prime:
                return strng[i]
    else:
        return repet1

print(first_non_repeating_letter('sTReSSt'))