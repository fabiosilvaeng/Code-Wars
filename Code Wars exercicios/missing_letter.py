#code wars Kata link: https://www.codewars.com/kata/5839edaa6754d6fec10000a2
def find_missing_letter(letras_inp):
    notin = []
    teste_maiusc = ((letras_inp[0]).upper())
    if letras_inp[0] != teste_maiusc:
        alfabeto ='abcdefghijklmnopqrstuvwxyz'
    else:
        alfabeto ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sinc = alfabeto.index(letras_inp[0])
    for i in range (sinc,(len(alfabeto))):
        if alfabeto[i] not in letras_inp:
            notin.append(alfabeto[i])
    return notin[0]


print (find_missing_letter(['O','P','Q','S']))