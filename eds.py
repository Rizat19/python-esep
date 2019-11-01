f=1
n=int(input('input n:'))
for i in range(n):
    i+=1
    f*=i
print('{} факториалы:'.format(n),f)