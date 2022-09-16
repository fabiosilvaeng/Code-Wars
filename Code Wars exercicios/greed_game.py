#code wars Kata link: https://www.codewars.com/kata/5270d0d18625160ada0000e4

def score(dice):
    pontos = {
        '1' : 1000,
        '6' : 600,
        '5' : 500,
        '4' : 400,
        '3' : 300,
        '2' : 200,
        1 : 100,
        5 : 50
    }
    pontuacao = 0
    for numdado in range (1,7):
        qtdappear = dice.count(numdado)
        if qtdappear >= 3:
            pontuacao += pontos[str(numdado)]
        if qtdappear > 3:
            pontuacao += ((qtdappear - 3)*pontos[numdado]) if (numdado == 1 or numdado == 5) else 0
        elif qtdappear > 0 and qtdappear < 3:
            pontuacao += (qtdappear*(pontos[numdado])) if (numdado == 1 or numdado == 5) else 0

    return pontuacao

print(score([3, 3, 3, 1, 3]))
 
