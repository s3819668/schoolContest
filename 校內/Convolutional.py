# ##寬高為原陣列-2
str1="4,4,107,108,52,226,44,96,198,240,39,91,114,240,203,240,247,132 "
str1=str1.split(",")
r=int(str1[1])
c=int(str1[0])
ans=[]
ori=[[0]*r for i in range(c)]
for i in range(c):
    for j in range(r):
        ori[i][j]=int(str1[2+i*(r)+j])
nr=r-2
nc=c-2
nori=[[0]*nr for i in range(nc)]
print(ori)
for i in range(nc):
    for j in range(nr):
        r=j+1
        c=i+1
        nori[i][j]=ori[c-1][r-1]-ori[c-1][r]+ori[c-1][r+1]-ori[c][r-1]+ori[c][r]-ori[c][r+1]+ori[c+1][r-1]-ori[c+1][r]+ori[c+1][r+1]
        ans.append(nori[i][j])
ans.sort()
print(ans[len(ans)-1])