#code wars Kata link: https://www.codewars.com/kata/514a024011ea4fb54200004b
def domain_name(url):
    bibli = ['www.','http://','https://',]
    lista=[]
    for i in bibli:
        if i in url:
            url = url.replace(i,'')
    lista = url.split('.')
    return lista[0]

print(domain_name("https://www.codewars.com/"))