import datetime
d1=input()
d1=d1.split("/")
print(d1)
for i in range(len(d1)):
    d1[i]=int(d1[i])
d2=input()
d2=d2.split("/")
for i in range(len(d2)):
    d2[i]=int(d2[i])
date1=datetime.datetime(d1[0],d1[1],d1[2])
date2=datetime.datetime(d2[0],d2[1],d2[2])
if (date1-date2).days>=0:
    print((date1-date2).days)
else:
    print((date2-date1).days)