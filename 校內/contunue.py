a="1112223334444555566667777"
now=1
max=0
for i in range(len(a)):
    if i <len(a)-1:
        if a[i]<=a[i+1] :
            now=now+1
        else:
            print("cut")
            if now>max:
                max=now
                now=1
    else:
        if now > max:
            max = now
            now = 1
    print("now",now)
print("max",max)


