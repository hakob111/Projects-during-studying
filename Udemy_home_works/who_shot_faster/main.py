def whos_first(p1, p2):
    a = p1.split(' ')
    b = p2.split(' ')
    c = [a ,b]
    count1 = 0
    count2 = 0
    for i in c[0]:
        if i != '':
            break
        count1 += 1
    for z in c[1]:
        if z != '':
            break
        count2 += 1
    if count1 &lt; count2:
        print (p1)
        print (p2)
        return ('p1')
    elif count1 &gt; count2:
        print (p1)
        print (p2)
        return ('p2')
    elif count1 == count2:
        print (p1)
        print (p2)
        return ('tie')