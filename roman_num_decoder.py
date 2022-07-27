def solution(a):
    roman_num= {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    lista_soma = []
    subtrai = 0
    for i in range (len(a)):
        lista_soma.append(roman_num[a[i]])
    for numero in range (len(lista_soma)):
        if numero < (len(lista_soma)-1):
            if lista_soma[numero]<lista_soma[numero+1]:
                subtrai += lista_soma[numero]
    result = sum(lista_soma) - (subtrai*2)
    return result


print(solution('MDCLXVI'))

