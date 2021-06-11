loop=1
while loop==1:
    user=input()
    oriuser=user
    if oriuser=="0":
        loop=0
        break
    check=0
    cl=0
    print("Original number was ",user)
    while check!=2 :
        rec=user
        array=[]
        str1=""
        str2=""
        for i in range(len(user)):
            array.append(user[i])
        array.sort()
        try:
            for i in range(len(user)):
               str1+=array[i]
               str2+=array[-i-1]
        except:
            pass
        int1=int(str1)
        int2=int(str2)
        if int1>int2:
            user=str(int1-int2)
            print(int1,"-",int2," = ",user)
        else:
            user=str(int2-int1)
            print(int2, "-", int1, " = ", user)
        if rec==user:
            check=2
        else:
            check=0
        cl+=1
    print("Chain length ",cl)
