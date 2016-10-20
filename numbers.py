def get_counts(wlist):
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    for word in wlist:
        if len(word) == 0:
            zero = zero + 1
        if len(word) == 1:
            one = one + 1
        if len(word) == 2:
            two = two + 1
        if len(word) == 3:
            three = three + 1
        if len(word) == 4:
            four = four + 1
        if len(word) == 5:
            five = five + 1
        if len(word) == 6:
            six = six + 1
        if len(word) == 7:
            seven = seven + 1
        if len(word) == 8:
            eight = eight + 1
        if len(word) == 9:
            nine = nine + 1
    return[zero, one, two, three, four, five, six, seven, eight, nine]