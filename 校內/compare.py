a=input("組")
b=int(a)
for i in range(b):
    c=input("兩組")
    c=c.split(" ")
    ans=[]
    for j in range(len(c)):
        ans.append(c[j])
    if ans[0]>ans[1]:
        print(">")
    if ans[0]==ans[1]:
        print("=")
    if ans[0]<ans[1]:
        print("<")