def calc_dice_scores(lst):
    c = []
    b = []
    for i in lst:
        if i[0]==i[1]:
            b.append(True)
        else:
            b.append(False)
    for i in range(len(lst)):
        c += lst[i]
    s = c
    if any(b):
        return 0
    else:
        return sum(s)