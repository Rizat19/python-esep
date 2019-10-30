f1=f2=1
print('1-element:',f1)
print('2-element:',f2)
print('fibonacci formula: f(n)=f(n-1)+f(n-2)')
n=int(input('n-element:'))
i=0
while i<n-2:
    f=f1+f2
    f1=f2
    f2=f
    i+=1
print('{}-element'.format(i+2),f2)
