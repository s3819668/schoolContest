loop=1
array=[]
times=input()
####測資輸入
while loop==1:
    user=input()
    if user=="0":
        break
    user=user.split(" ")
    for i in range(len(user)):
        ####補成一對
        if i != 0:
            array.append(user[0])
            array.append(user[i])
        ####
    print(array)
####

count=0
pastSet=set()#上一個迴圈燒到的
nowSet=set()#當前已燒到的
while len(array)>2:
    pastSet=nowSet.copy()###複製一份 後續沒改變就跳出迴圈節省時間
    inum=-1
    ####找出只出現一次的check表示出現幾次
    for i in range(len(array)):
        check=0
        for j in range(len(array)):
            if array[j]==array[i]:
                check+=1
            if check>=2:
                break
        if check==1:
            only=array[i]
            inum=i ####葉子
            break
    ####
    ####沒重複就表示結束
    if inum==-1:
      break
    ####

    ####燒掉葉子與枝
    else:
      if inum%2==0:
          nowSet.add(array[i + 1])
          del array[i]
          del array[i+1]
      elif inum%2==1 :
          nowSet.add(array[i - 1])
          del array[i]
          del array[i-1]
    ####

    ####有被燒到就計數器+1
    if nowSet!=pastSet:
      count += 1
    print(nowSet)
    print(array)
print(count)

