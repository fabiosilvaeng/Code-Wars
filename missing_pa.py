## encontrar numero perdido na progressão aritimetica
def find_missing (a):
    vet = a
    raz = (vet[-1] - vet[0])/len(vet)
    for i in range (1,len(vet)):
        if (vet[i] - vet[i-1] ) != raz:
            seq = vet[0]+(raz*i)
    return int(seq)  
         
print (find_missing([1, 2, 3, 4, 6, 7, 8, 9]))