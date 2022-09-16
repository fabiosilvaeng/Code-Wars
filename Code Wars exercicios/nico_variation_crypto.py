#code wars Kata link: https://www.codewars.com/kata/5968bb83c307f0bb86000015
def nico(key,msg):

    srted = ''.join(sorted(key))
    number = []
    txt = ''
    dicio = {}

    if len(key) >= len(msg):
        msg += ((len(key)-len(msg))*' ')
    
    div = 1 if len(key) >= len(msg) else int(len(msg)/len(key)) if len(msg)%len(key) == 0 else (int(len(msg)/len(key))+1)

    for index in key:
        number.append((srted.index(index))+1)

    for k in range (div):
        dicio = {}
        fraction = msg[(len(key))*k:(len(key))*(k+1)]
        if len(fraction) <= len(key):
            fraction = fraction + ((len(key)-len(fraction))*' ') if len(fraction) <= len(key) else fraction

        for i in range (len(fraction)):
            dicio[number[i]] = fraction[i]

        for u in sorted(number):
            txt += dicio[u] 

    return txt

print(nico('crazy','secretinformation'))




