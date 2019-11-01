d={'a','e','i','o','u'}
soz=input()
def a():
    s=list(soz)
    s1=''
    for i in s:
        if i in d:
            i='*'
        s1+=i
    print(s1)

a()
    
        

        