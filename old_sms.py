def presses (a:str):

    nome = a.upper()

    tecla ={
        '1':['1'],
        '2':['A','B','C','2'],
        '3':['D','E','F','3'],
        '4':['G','H','I','4'],
        '5':['J','K','L','5'],
        '6':['M','N','O','6'],
        '7':['P','Q','R','S','7'],
        '8':['T','U','V','8'],
        '9':['W','X','Y','Z','9'],
        '0':[' ','0'],
        'asterisco':['*'],
        'hashtag':['#']
    }
    cont = 0
    for teclado in tecla.values(): 
        lista = teclado
        for letra_nome in nome:
            if letra_nome in lista:
                cont += (lista.index(letra_nome)+1)
    return cont

print (presses('ZE FPG11J2IQV*5GS8D'))
