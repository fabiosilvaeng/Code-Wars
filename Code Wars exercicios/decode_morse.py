#code wars Kata link: https://www.codewars.com/kata/decode-the-morse-code
def decode_morse(morse_code):
    morse = {
        '.-.-.-' : '.',
        '-.-.--':'!',
        '' : '',
        '.-' : 'a',
        '-...' : 'b',
        '-.-.' : 'c',
        '-..' : 'd',
        '.' : 'e',
        '..-.' : 'f',
        '--.' : 'g',
        '....' : 'h',
        '..' : 'i',
        '.---' : 'j',
        '-.-' : 'k',
        '.-..' : 'l',
        '--' : 'm',
        '-.' : 'n',
        '---' : 'o',
        '.--.' : 'p',
        '--.-' : 'q',
        '.-.' : 'r',
        '...' : 's',
        '-' : 't',
        '..-' : 'u',
        '...-' : 'v',
        '.--' : 'w',
        '-..-' : 'x', 
        '-.--' : 'y',
        '--..' : 'z',
        '...---...' : 'SOS'
    }
    txt = ''
    cont = 0
    continv = -1
    letra = morse_code.split(' ')

    for i in range (len(letra)):
        if letra[i] == '' and i+1 < len(letra) and letra[i+1] == '':
            txt += ' '
        if letra[i] in morse.keys():
            txt += morse[letra[i]]

    while txt[cont] == ' ':
        cont += 1
    while txt[continv] == ' ':
        continv -= 1

    if continv < -1:
        return txt[cont:(continv+1)].upper()
    else:
        return txt[cont:].upper() 



print(decode_morse('.... . -.--   .--- ..- -.. .'))