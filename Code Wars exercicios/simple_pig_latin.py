#code wars Kata link: https://www.codewars.com/kata/520b9d2ad5c005041100000f
def pig_it(text):
    lista = text.split()
    conv = ''
    for i in lista:
        if i.isalpha():
            strng = i
            if len(strng) > 1:
                strng = strng + strng[0]
                conv += strng[1:]+'ay '
            else:
                conv += strng + 'ay '
        else:
            conv += str(i)
    if conv[-1] == ' ':
        return conv[:-1]
    else:
        return conv
          
    
print(pig_it('O tempora o mores !'))