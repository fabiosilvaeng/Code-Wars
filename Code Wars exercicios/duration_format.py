#code wars Kata link : https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    
    parametros = [31536000,365,24,60,60]
    time = ['year','day','hour','minute','second']
    txt = ''
    final = []

    calc = seconds/parametros[0]
    txt += str(int(calc)) + '*'
    flt = float(calc) - int(calc)

    for u in range (1,len(parametros)):
        if u == 4:
            calc = round(flt * parametros[u])
        else:
            calc = round((flt * parametros[u]),15)
        txt += str(int(calc)) + '*'
        flt = float(calc) - int(calc)
    
    separar = txt.split('*')

    txt = ''

    for i in range (0,5):
        if separar[i] != '0':
            final.append(str(separar[i]+' '+time[i]) + 's' if int(separar[i]) > 1 else str(separar[i]+' '+time[i]))

    if seconds == 0:
        txt = 'now'
    elif len(final) > 2:
        for k in final[:-2]:
            txt += k+', '
        txt += final[-2]+' and '
        txt += final[-1]
    elif len(final) == 2:
        txt += final[-2]+' and '
        txt += final[-1]
    else:
        txt += final[0]

    return txt
    

print(format_duration(79000599896)) 




