def street_fighter_selection (a,b,c):
    lista = (a)
    fighters = lista[0] + lista[1]
    if b[0]==0: 
        pos_atual = b[1]
    else:
        pos_atual = b[1]+6
    moves = c
    hist =[]
    for i in moves:
        if i == 'up' and pos_atual>5:
            pos_atual -=6
            hist.append(fighters[pos_atual])
        elif i == 'up':
            hist.append(fighters[pos_atual])
        elif i == 'down' and pos_atual<=5:
            pos_atual +=6
            hist.append(fighters[pos_atual])
        elif i == 'down':
            hist.append(fighters[pos_atual])
        elif i =='left'and (pos_atual==0 or pos_atual==6):
            pos_atual +=5
            hist.append(fighters[pos_atual])
        elif i == 'left':
            pos_atual -=1
            hist.append(fighters[pos_atual])
        elif i =='right' and (pos_atual==5 or pos_atual==11):
            pos_atual -=5
            hist.append(fighters[pos_atual])
        elif i =='right':
            pos_atual +=1
            hist.append(fighters[pos_atual])
    return (hist)

print(street_fighter_selection([
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
],(0,0),['up','up','up']))



