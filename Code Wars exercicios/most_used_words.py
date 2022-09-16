# code wars Kata link: https://www.codewars.com/kata/51e056fe544cf36c410000fb
def top_3_words(txt):
    import re
    def top3_words(lista,top_word1,top_word2):
        biggest = (0,'')
        for cont in lista:
            if cont != top_word1 and cont != top_word2:
                tuple = (lista.count(cont),cont)
                biggest = tuple if tuple[0] > biggest[0] else biggest
        if biggest[-1] != '':
            return biggest[-1]
    asci = ['!','"','#','$','%','&','(',')','*','+',',','¨','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    no_acce = []
    top3_list = []

    texto_tratado = ''

    for word in txt:
        strng = word
        for special in asci:
            if special in strng:
                strng = strng.replace(special,' ')
        texto_tratado += strng

    lista = texto_tratado.split(' ')

    for strng in lista:
        if strng.isalpha():
                no_acce.append(strng.lower())
        elif "'" in strng:
            reg_teste = re.match("^([A-Za-z]+?)[']?[A-Za-z]+[']?([A-Za-z]+?)$",strng)
            if reg_teste:
                no_acce.append(strng.lower())
            else:
                reg_teste = re.match("^[']{0,2}?[A-Za-z]+?[']{0,2}?[A-Za-z]+?[']{0,2}?$",strng)
                if reg_teste:
                    no_acce.append(strng.lower())

    top1 = top3_words(no_acce,'*','*')
    top3_list.append(top1)

    top2 = top3_words(no_acce,top1,'*')
    top3_list.append(top2)

    top3 = top3_words(no_acce,top1,top2)
    top3_list.append(top3)

    while None in top3_list:
        top3_list.remove(None)

    return top3_list


print(top_3_words(

"xpDVYo:xpDVYo_? ?,zmP'Jy'kz;,,;xpDVYo,_/._iLY?,:zmP'Jy'kz!_,/.zmP'Jy'kz?-zmP'Jy'kz.?xpDVYo: !iLY.,.iLY_:, xpDVYo.xpDVYo,/iLY:zmP'Jy'kz - zmP'Jy'kz?.?xpDVYo/!_-zmP'Jy'kz;!_iLY_ / !zmP'Jy'kz!?zmP'Jy'kz::iLY._ -iLY.  zmP'Jy'kz//:zmP'Jy'kz-:/;zmP'Jy'kz.:;iLY-!!?zmP'Jy'kz-!zmP'Jy'kz /_;?xpDVYo/,xpDVYo?zmP'Jy'kz!zmP'Jy'kz_xpDVYo._!zmP'Jy'kz;,/?zmP'Jy'kz:._;:xpDVYo ;-"

))
        