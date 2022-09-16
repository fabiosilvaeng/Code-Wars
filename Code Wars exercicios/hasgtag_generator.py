#code wars Kata link: https://www.codewars.com/kata/52449b062fb80683ec000024
def generate_hashtag(s):
    hashtag = ''
    lista = s.split(' ')
    for i in lista:
        hashtag += i.capitalize()
    if len(hashtag) > 140 or s == '':
        return False
    else:
        return '#' + hashtag


print(generate_hashtag('c i n'))