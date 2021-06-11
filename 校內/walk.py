a=input("組")
b=int(a)
d=[]
count = 0
x=0
y=0
for i in range(b):
    c=input("4組")
    c=c.split(" ")
    for j in range(len(c)):
        d.append(int(c[j]))
    print(d)
    if d[0]-d[2] >0:
        x=d[0]-d[2]
    else:
        x=d[2]-d[0]
    if d[1]-d[3]>0:
        y=d[1]-d[3]
    else:y=d[3]-d[1]
    if x==y and x!=0:
        count=1;
    else:
        if(d[0]!=d[2]):
            count=count+1
        if(d[1]!=d[3]):
            count=count+1
    print(count)
    count=0
    d.clear()