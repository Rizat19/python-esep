n=['Rizat']
l=[]
for i in n:
    f=len(i)
    for item in range(1,f+1):
        d=n[0][item-1]
        print(d)
        l.append(d)
print(l)