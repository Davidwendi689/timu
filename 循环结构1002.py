a=int(input())
count=1
for i in range(1,a+1):
    for j in range(count,count+i):
        print("%4d"%j,end="")
    print()
    count+=i