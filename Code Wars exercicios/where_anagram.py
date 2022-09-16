#code wars Kata link: https://www.codewars.com/kata/523a86aa4230ebb5420001e1
def anagrams(word, words):

    word_sorted = list(word)
    word_sorted = sorted(word_sorted)

    correto = []

    for i in words:
        teste = list(i)
        teste = sorted(teste)
        if teste == word_sorted:
            correto.append(i)

    return correto


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))