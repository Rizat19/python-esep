a=[]
sum=0
k=0
avg=0
while True:
    i=input()
    if i=='ok':
        break
    a.append(i)
    sum+=int(i)
    k+=1
    avg=sum/k
print(a,'\nsumma ',sum,'\navg ',avg)
    
    
    