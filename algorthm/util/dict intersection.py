def intersection(a,b):
    temp= a if len(a)>len(b) else b
    res=[]
    for i in temp.keys():
        if i in b: res.append(i)
    return res