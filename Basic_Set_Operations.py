a = [15, 25, 35, 45, 5, 5, 25]
b = [45, 5, 65, 75, 85, 75,45]

def intersection_using_dic():
    D1 = {}
    for i in a:
        D1[i] = 1
    c = []
    D2 = {}
    for i in b:
        D2 [i] = 1
    for i in D1.keys():
        if i in D2:
            c.append(i)
    print("The intersection of two lists is ", c)

def union_using_dic():
    D = {}
    u = []
    for i in a:
        if i not in D:
            u.append(i)
            D[i] = 1
    for i in b:
        if i not in D:
            u.append(i)
            D[i] = 1
    print("The union of two lists is ", u)
    

intersection_using_dic()
union_using_dic()