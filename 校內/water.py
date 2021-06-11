x=[]
y=[]

target=input().split(" ")
s=int(target[0])
a=int(target[1])
F=int(target[2])
for i in range(F):
    position=input().split(" ")
    x.append(int(position[0]))
    y.append(int(position[1]))
x.sort()
y.sort()
print(x)
print(y)
if F%2:
    print("Street:",x[int(F/2)],"Avenue:",y[int(F/2)])
else:
    print("Street:",x[int((F-1)/2)],"Avenue:",y[int((F-1)/2)])