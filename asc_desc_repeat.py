def ascend_descend(length, minimum, maximum):
    sequence =''
    for a in range (minimum,maximum+1):
        sequence += str(a)
    for d in range (maximum-1,minimum,-1):
        sequence += str(d)
    sequence += (sequence)*length
    sequence = sequence[0:length]
    return sequence

print(ascend_descend(14, 1, 2))

