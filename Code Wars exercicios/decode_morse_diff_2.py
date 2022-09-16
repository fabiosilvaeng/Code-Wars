#code wars Kata link: https://www.codewars.com/kata/54b72c16cd7f5154e9000457
def decode_bits(bits):
    def condicional(index,bit,caracter):
        if index in bit:
            bit = bit.replace(index,caracter)
            return bit
        else:
            return bit 

    def zero_count(bit,start_or_end,string,contador):
        while bit[start_or_end] == string:
            start_or_end += contador 
        return start_or_end

    ini = zero_count(bits,0,'0',1)
    fin = zero_count(bits,-1,'0',-1)
    bits = bits[ini:(fin+1)] if fin < -1 else bits[ini:]

    if '0' not in bits:
        bits = '.'  
    else:
        qtd_0 = bits.count('0')
        qtd_1 = bits.count('1')

        freq_termo = [i.count('1') for i in bits.split('0')] if qtd_1 < qtd_0 else [i.count('0') for i in bits.split('1')]

        while 0 in freq_termo:
            freq_termo.remove(0)
        
        ponto = '1'*(min(freq_termo))
        empty = '0'*(min(freq_termo))
        traco = '1'*(min(freq_termo)*3)
        letter_space = '0'*(min(freq_termo)*3)
        word_space = '0'*(min(freq_termo)*7)
        
        mean = {traco : '-', ponto : '.', word_space : '   ', letter_space : ' ', empty : '', '0' : ''}

        for i in mean:
            bits = condicional(i,bits,mean[i])          

    return bits

print(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))




