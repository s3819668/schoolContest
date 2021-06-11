def count(n,k):
    num=0
    if n==0:
        return 0
    if k==0:
        return 1
    else:
        i=0
        while i<n and k-i>=0:
            num+=count(n-1,k-i)
            i+=1
    return num
times=int(input())
array=[]
for j in range(times):
    data=input()
    data=data.split(" ")
    ans=count(int(data[0]),int(data[1]))
    array.append(ans)
    data.clear()
for k in range(len(array)):
    print(array[k])
