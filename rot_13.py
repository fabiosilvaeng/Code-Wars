def rot13(message):
    cripto =''
    alfa ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for u in (message):
        if u.isnumeric() or u == ' ' or u not in alfa:
            cripto += u
        if u.isupper():
            lista = alfa[26:]
        else: 
            lista = alfa[:26]
        for i in range (len(lista)):
            if u == lista[i]:
                sobra = len(lista) - i
                if sobra > 13:
                    cripto += lista[i+13]
                else:
                    cripto += lista[13-sobra]
    return cripto

print(rot13('123fABIO`**/!!abc 99'))

