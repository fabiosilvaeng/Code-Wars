# code wars Kata link: https://www.codewars.com/kata/51fc12de24a9d8cb0e000001
def valid_ISBN10(isbn):
    if len(isbn) < 10 or len(isbn) > 10 or isbn.isalpha() or (isbn[-1].isalpha() and isbn[-1] !='X') or ('X' in isbn and isbn[-1] !='X'):
        return False
    else:
        isbn = '0'+isbn
        calc = 100 if isbn[-1] == 'X' else 0

        for i in range (len(isbn)):
            if isbn[i] != 'X':
                calc += (int(isbn[i])*i)
        calc = calc%11

        return True if calc == 0 else False

print(valid_ISBN10('47340172714'))