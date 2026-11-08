x,y=map(int,input().split())
count=0
for i in range(x,y+1):
    a=0
    for j in range(0,len(str(i))):
        a+=int(str(i)[j])
    if a%5==0:
        count+=1
print(count)