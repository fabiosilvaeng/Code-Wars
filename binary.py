def count_bits (n):
    n=bin(n).split('0b')[-1]
    cont = 0
    for i in n:
        if i == '1':
            cont = cont+1
    return cont

