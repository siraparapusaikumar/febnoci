a=0
b=1
c=a+b
res=[]
while b<=50:
    c=a+b
    res.append(b)
    a,b=b,c
print(' '.join(map(str,res))) 