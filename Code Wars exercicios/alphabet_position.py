#code wars Kata link: https://www.codewars.com/kata/546f922b54af40e1e90001da
def alphabet_position(text):
    min = text.lower()
    alfa = '*abcdefghijklmnopqrstuvwxyz'
    numerico =''
    for i in min:
        for u in range (len(alfa)):
            if i == alfa[u]:
                numerico += ' '+str(u)

    return numerico[1:]

print(alphabet_position('fabio'))
