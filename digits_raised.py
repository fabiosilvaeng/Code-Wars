# code wars Kata link: https://www.codewars.com/kata/5626b561280a42ecc50000d1
def sum_dig_pow(a,b):
    lista_ok = []
    for i in range (a,b+1):
        soma = 0
        string = str(i)
        for u in range (1,len(string)+1):
            calculo_algarismo = (int(string[u-1]))**u
            soma += calculo_algarismo
        if i == soma:
            lista_ok.append(soma)

    return lista_ok


print (sum_dig_pow(10, 100))