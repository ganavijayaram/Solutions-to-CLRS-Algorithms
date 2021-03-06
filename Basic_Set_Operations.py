a = [15, 25, 35, 45, 5, 5, 25]
b = [45, 5, 65, 75, 85, 75,45]
a = [1, 2, 3]
b = [1, 5, 7, 8, 2, 3, 10]
d = [3, 4, 2, 2, 1, 2, 10]

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
    return c

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

def difference():
    D1 = {}
    D2 = {}
    c = []
    for i in b:
        D2[i] = 1
    for i in a:
        D1[i] = 1
    for i in D1.keys():
        if i not in D2:
            c.append(i)
    print("A - B = ", c)

def symmetric_difference():
    D1 = {}
    D2 = {}
    c = []
    for i in a:
        D1[i] = 1
    for i in b:
        D2[i] = 1
    for i in D1.keys():
        if i not in D2:
            c.append(i)
    for i in D2.keys():
        if i not in D1:
            c.append(i)
    print("Symmetric Difference is ", c)

def disjoint():
    if(intersection_using_dic() == []):
        print("Disjoint Sets")
    else:
        print("Not Disjoint Sets")

def subset():
    D1 = {}
    for i in b:
        D1[i] = 1
    for i in a:
        if i not in D1:
            print("A not subset of B")
            break
    else:
        print("A is a subset of B")

def superset():
    D1 = {}
    for i in b:
        D1[i] = 1
    for i in a:
        if i not in D1:
            print("B is not superset of A")
            break
    else:
        if(len(D1.keys()) >= len(a)):
            print("B is superset of A")

def remove_duplicates():
    D = {}
    for i in d:
        D[i] = 1
    lst = []
    for keys in D.keys():
        lst.append(keys)
    print("After removing duplicates ", lst)

intersection_using_dic()
union_using_dic()
difference()
symmetric_difference()
disjoint()
subset()
superset()
remove_duplicates()
