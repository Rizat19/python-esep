a=input('soz:')
l=[]
for item in range(len(a)):
    #print(item)
    z=a.split()
    print(z[0][item])
    l.append(z[0][item])
print(l)