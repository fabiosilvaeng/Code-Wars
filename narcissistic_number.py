def narcissistic (a):
    string_num = str(a)
    length_num = len(str(a))
    acum = 0
    for i in range (length_num):    
        acum += (int(string_num[i]))**length_num
    if a == acum:
        return True
    else:
        return False

print (narcissistic(371))


