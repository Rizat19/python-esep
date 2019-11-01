
l=[]
while True:
    name=input('name:')
    if name=='ok':
        break
    l.append(name)
print(l)

a=list(l)
i=0
while i<len(a):
    ball=int(input('ball:'))
    a.append(ball)
    i+=1
print(a)

