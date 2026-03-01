a=[['black'],['brown'],['red'],['orange'],['yellow'],['green'],['blue'],['violet'],['grey'],['white']]
for i in range(10):
    a[i]+=[i,10**i]
x,y,z=input(),input(),input()
for m,n,o in a:
    if m==x:
        x1=n
    if m==y:
        y1=n
    if m==z:
        z1=o
print((x1*10+y1)*z1)