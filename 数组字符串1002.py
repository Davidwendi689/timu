x,y=map(int,input().split())
count=0
str_1=str(y)
for i in range(1,x+1):
    str_i=str(i)
    count+=str_i.count(str_1)
print(count)