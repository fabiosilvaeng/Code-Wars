#code wars Kata link: https://www.codewars.com/kata/54edbc7200b811e956000556
def count_sheeps(lista_de_ovelhas):
    count = 0
    for ovelhas in lista_de_ovelhas:
        if ovelhas == True:
            count = count + 1   
    return count

print(count_sheeps([ True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True ]))
