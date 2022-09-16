#code wars Kata link: https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc
def is_a_valid_message(message):
    num = ''
    strng = ''
    validation = 0
    
    if message == '':
        return True
    elif message[0].isalpha() or message[-1].isnumeric():
        return False
    else:
        for i in message:
            if i.isnumeric():
                num += i
                strng += '*'
            else:
                strng += i
                num += '*'

        strng = strng.split('*')
        num = num.split('*')

        while '' in strng:
            strng.remove('')
        while '' in num:
            num.remove('')

        for u in range (len(num)):
            if int(num[u]) == len(strng[u]):
                validation +=1
        
        if validation == len(num):
            return True
        else:
            return False
        


print(is_a_valid_message('4code13hellocodewars'))