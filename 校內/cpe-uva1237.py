times=int(input())
datatimes=int(input())
array=[]
ans=[]

def check(price):
    global array
    global ans
    for i in array:
        if price >= int(i['coml']) and price<=int(i['comh']):
            ans.append(i)
    if len(ans)==1:
        print(ans)
        return ans[0]['com']
    else:
        return "UNDETERMINED"

for i in range(datatimes):
    data=input().split(" ")
    com=data[0]
    coml=data[1]
    comh=data[2]
    array.append({'com':data[0],'coml':data[1],'comh':data[2]})
# for i in array:
#     if int(i['coml'])<=50000:
user=int(input())
for i in range(user):
    price=int(input())
    print(check(price))
    ans.clear()

