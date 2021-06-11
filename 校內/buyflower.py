array=input().split(" ")
count=0
for i in range(len(array)):
    array[i]=int(array[i])
array.sort()
print(array)
for i in range(int(len(array)//3),len(array)):
    count+=array[i]
print(count)
