#code wars Kata link: https://www.codewars.com/kata/525caa5c1bf619d28c000335
def is_solved(board):
    def diagonal_insert(game,pos1,pos11,pos2,pos22,pos3,pos33):
        lista = []
        lista.append(game[pos1][pos11])
        lista.append(game[pos2][pos22])
        lista.append(game[pos3][pos33])
        return lista

    x_win = [1,1,1]
    o_win = [2,2,2]

    for line in board:
        if line == x_win:
            return 1
        elif line == o_win:
            return 2
    
    for index in range (0,3):
        x_o_verify = []
        for line in board:
            if len(x_o_verify) < 3:
                x_o_verify.append(line[index])
        if x_o_verify == x_win:
            return 1 
        elif x_o_verify == o_win:
            return 2
    
    x_o_verify = diagonal_insert(board,0,0,1,1,2,2)

    if x_o_verify == x_win:
        return 1
    elif x_o_verify == o_win:
        return 2
    
    x_o_verify = diagonal_insert(board,0,2,1,1,2,0)

    if x_o_verify == x_win:
        return 1
    elif x_o_verify == o_win:
        return 2

    zeros = ''
    for lists in board:
        for number in lists:
            zeros += str(number)
    
    return -1 if '0' in zeros else 0

print(is_solved(

[[1, 2, 1],
 [0, 0, 2],
 [1, 1, 2]]
))
