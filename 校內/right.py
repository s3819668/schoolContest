######way1#####
a='cde12dqceq2'
b=[]
c=[]
for i in range(len(a)):
    b.append(a[i])
b.reverse()
for i in range(len(a)):
    if len(c)==0:
        c.append(b[0])
    for j in range(len(c)):
        check = 0
        if b[i] == c[j]:
            check = 1
            break
    if check == 0:
        c.append(b[i])
c.reverse()
print(c)

#####way2#####
old=set()
now=set()
array=[]
ans=[]
for i in range(len(a)):
    array.append(a[i])
array.reverse()
for i in range(len(array)):
    now.add(array[i])
    if now!=old:
        ans.append(array[i])
        old.add(array[i])
ans.reverse()
print(ans)