def is_twinprime(n):
    numeros = {'central':n,'antecessor':n-2,'sucesor':n+2}
    qtd_primos = 0
    e_primo = 0 
    for i in range (2,n+1):
        if n%i == 0:
            e_primo += 1
    if e_primo > 1:
        return False
    else:
        for u in numeros.values():
            divisivel = 0
            for i in range (2,u+1):
                if u%i == 0:
                    divisivel += 1 
            if divisivel == 1 and n !=9 :
                qtd_primos += 1
        if qtd_primos > 1:
            return True
        else:
            return False




    
    
    


print (is_twinprime(9))
