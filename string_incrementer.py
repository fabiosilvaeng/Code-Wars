def increment_string(strng):
    nums = ['0','1','2','3','4','5','6','7','8','9']
    parte_numerica = '' 

    if strng == '' or strng[-1] not in nums:
        strng = strng+'1'
    else:
        for i in range (1,len(strng)+1):
            parte_numerica += strng[-i]
            if strng[-i] not in nums:
                break

        parte_numerica = parte_numerica[::-1]

        if parte_numerica[0] not in nums:
            parte_numerica = parte_numerica[1:]

        strng = strng[0:-len(parte_numerica)]
        parte_numerica = str((int('10'+parte_numerica)+1))

        if parte_numerica[1] != '0':
            parte_numerica = parte_numerica[1:]
        else:
            parte_numerica = parte_numerica[2:]

    return strng+parte_numerica


print (increment_string(""))

# "HX%q B854791601>FL'4A#427973^<`>[6578(`%WE2{w5823045xe017443797121"


