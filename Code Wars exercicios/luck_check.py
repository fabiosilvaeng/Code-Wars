#code wars Kata link: https://www.codewars.com/kata/5314b3c6bb244a48ab00076c
def luck_check(string):
    half_1 = 0
    half_2 = 0
    if len(string)%2 == 0: 
        metade = len(string)/2
        for i in range (int(metade)):
            half_1 += int(string[i])
        for u in range (int(metade),int(metade*2)):
            half_2 += int(string[u])
    else:
        metade = (int(len(string)/2)+1)
        for i in range (int(metade)-1):

            half_1 += int(string[i])
        for u in range (int(metade),int(metade*2)-1):
            half_2 += int(string[u])

    if half_1 == half_2:
        return True
    else:
        return False
