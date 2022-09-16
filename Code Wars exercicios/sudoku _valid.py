# code wars Kata link: https://www.codewars.com/kata/529bf0e9bdf7657179000008
def valid_solution(board):
    sort = [1,2,3,4,5,6,7,8,9]
    boolist = []
    for line in board:
        if 0 in line:
            return False
        boolist.append(True if sorted(line) == sort else False)
    
    column_verify = []

    for column in range (0,9):
        for line in board:
            if len(column_verify) <= 9:
                column_verify.append(line[column])
        boolist.append(True if sorted(column_verify) == sort else False) 
        column_verify = []

    for line in board:
        for three in range (0,3):
            if len(column_verify) <= 8:
                column_verify.append(line[three])
    boolist.append(True if sorted(column_verify) == sort else False) 

    return False if False in boolist else True



print(valid_solution([

[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]

]))