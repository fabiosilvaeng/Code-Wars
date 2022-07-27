def digital_root(n):
    string = str(n)
    acum = 0
    while len(string) != 1:
        for i in string:
            acum += int(i)
        string = str(acum)
        acum = 0
    return int(string)

print(digital_root(493193))
