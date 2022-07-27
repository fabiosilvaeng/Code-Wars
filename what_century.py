def what_century(year):
    ordinal = ['th','st','nd','rd','th','th','th','th','th','th']
    if len(year) < 3:
        seculo ='1'
    else:
        seculo = str(year[:-2])
    
    if int(year[len(seculo):]) > 0:
        seculo = str(int(seculo)+1)
    
    if int(seculo) < 4 or int(seculo) > 20:
        seculo = seculo + ordinal[int(seculo[-1])]
    else:
        seculo = seculo + ordinal[-1]

    return seculo





print(what_century("1234"))