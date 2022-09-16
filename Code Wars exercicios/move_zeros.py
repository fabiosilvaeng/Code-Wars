#code wars Kata link: https://www.codewars.com/kata/52597aa56021e91c93000cb0
def move_zeros(lst):
    qtd = 0
    while 0 in lst:
        lst.remove(0)
        qtd += 1
    while qtd > 0:
        lst.append(0) 
        qtd -= 1
    return lst




print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
