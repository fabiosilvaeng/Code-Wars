#code wars Kata link: https://www.codewars.com/kata/513e08acc600c94f01000001
def rgb(r,g,b):

    def to_hex(n):
        n = 255 if n > 255 else 0 if n < 0 else n
        hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        div = int(n/16)
        resto = n%16
        return hex[div]+hex[resto]
    
    red = to_hex(r)
    green = to_hex(g)
    blue = to_hex(b)

    return red+green+blue

print(rgb(300,300,300))