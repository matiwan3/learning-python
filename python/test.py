
a=[]

xmax=30
ymax=40
step=5 
t=0

for x in xrange(0,xmax+1,step):
    a.append([])
    for y in xrange(20,ymax+1,step):
        a[t].append((x,y))
    print (f"Row {t+1}: {a[t]}")
    t+=1
    # list(range(5, 20, 3)) (start,stop,step)