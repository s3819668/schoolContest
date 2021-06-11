loop=1
while loop==1:
  ans=set()
  num=input().split(" ")
  npeople=int(num[0])
  mpair=int(num[1])
  if npeople==0 and mpair==0:
    loop=0
    break
  array=[[""]*2 for i in range(npeople)]
  for i in range(npeople):
    array[i][0]=i
    array[i][1]=i
  for i in range(mpair):
    people=input().split(" ")
    p1=int(people[0])
    p2=int(people[1])
    array[p2-1]=array[p1-1]
  for i in range(npeople):
    ans.add(array[i][1])
  print(len(ans))