#code wars Kata link: https://www.codewars.com/kata/60cc93db4ab0ae0026761232
def arrange (s):
    if len(s)%2 > 0:
        meio = int(len(s)/2)
    t = []
    if len(s) == 1:
        t = s
    for i in range (len(s)-1):
        if i < ((len(s)-1)-i):
            if i%2 == 0:
                t.append(s[i])
                t.append(s[((len(s)-1)-i)])
            else:
                t.append(s[((len(s)-1)-i)])
                t.append(s[i])
        elif i == ((len(s)-1)-i):
            t.append(s[meio])
    return t