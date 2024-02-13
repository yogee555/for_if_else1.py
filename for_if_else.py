l1 = [1,2,3,4,5,6]
l2 = [1,3,8,9,5]
for i in l1:
    if i in l2:
        pass
    else:
        print(i)
    for i in l2:
        if i in l1:
            pass
        else:
            print(i)
