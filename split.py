text='Rizat, MAdi, Meruyert, Meiirzhan are students! They studying in KazNU'
q=text.split(',')
print(q)

l=[]
for i in q:
    s=i.split('!')
    l.append(s)
print(l)

l1=[]
for i in q:
    if '!' not in i:
        l1.append(i)
    else:
        s1=i.split('!')
        for s in s1:
            l1.append(s)
print(l1)