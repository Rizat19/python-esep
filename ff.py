def f(n):
    if n==1 or n==0:
        return 1
    return n*f(n-1)

a=int(input('san engiz:'))
s=f(a)
print('{} -factorialy:'.format(a),s)
