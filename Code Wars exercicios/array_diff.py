#code wars Kata link: https://www.codewars.com/kata/523f5d21c841566fde000009
def array_diff(a,b):    
    for i in range (len(b)):
        while b[i] in a :
            a.remove(b[i])
    return(a)

print (array_diff([1,2,3,4,4,4,4,4,4,4], [2,4]))