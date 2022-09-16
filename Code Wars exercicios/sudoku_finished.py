# code wars Kata link: https://www.codewars.com/kata/53db96041f1a7d32dc0004d2
def done_or_not(board):
    sudoku = board
    count = 0
    ordenate = [1,2,3,4,5,6,7,8,9]
    column_verify = []
    grid_verify = []

    for line in sudoku:
        linha = line
        lista = sorted(linha)
        if ordenate == lista:
            count += 1

    for coluna in range (0,9):
        for termo in sudoku:
            if len(column_verify) <= 8: 
                column_verify.append(termo[coluna])

        if sorted(column_verify) == ordenate:
            count += 1
            column_verify = []

    for list in sudoku:
        for pos in range (0,3):
            if len(grid_verify) <= 8:
                grid_verify.append(list[pos])
    
    if sorted(grid_verify) == ordenate:
        count += 1

    return 'Finished!' if count == 19 else 'Try again!'

print(done_or_not([
[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[2, 3, 4, 5, 6, 7, 8, 9, 1], 
[3, 4, 5, 6, 7, 8, 9, 1, 2], 
[4, 5, 6, 7, 8, 9, 1, 2, 3], 
[5, 6, 7, 8, 9, 1, 2, 3, 4], 
[6, 7, 8, 9, 1, 2, 3, 4, 5], 
[7, 8, 9, 1, 2, 3, 4, 5, 6], 
[8, 9, 1, 2, 3, 4, 5, 6, 7], 
[9, 1, 2, 3, 4, 5, 6, 7, 8]
]))


