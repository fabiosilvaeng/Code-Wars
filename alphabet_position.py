def alphabet_position(text):
    min = text.lower()
    alfa = '*abcdefghijklmnopqrstuvwxyz'
    numerico =''
    for i in min:
        for u in range (len(alfa)):
            if i == alfa[u]:
                numerico += ' '+str(u)

    return numerico[1:]

print(alphabet_position('fabio'))