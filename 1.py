##s = 'I am a student! I live in Almaty. This is my Unversity-KazNU!'
##sB = s.split('.')
##print(sB)
##
##for i in sB:
##    print(i)
##s_s = []
##for i in sB:
##    s_i = i.split('!')
##    s_s.append(s_i)
##print(s_s)
##
##s_s1 = []
##for i in sB:
##    if '!' not in i:
##        s_s1.append(i)
##    else:
##        s_i_l = i.split('!')
##        for s_i in s_i_l:
##            s_s1.append(s_i)
##
##print(s_s1)
##
##

s='Hello. How are you? I am ok, and you?'
print(s)
sp=s.split('?')
print(sp)

l=[]
for i in sp:
    d=i.split('.')
    l.append(d)
print(l)

l1=[]
for i in sp:
    if '.' not in i:
        l1.append(i)
    else:
        d1=i.split('.')
        for d in d1:
            l1.append(d)
print(l1)

for i in l1:
    if i=='':
        l1.pop()
print(l1)






