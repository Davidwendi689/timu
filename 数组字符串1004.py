L,M=map(int,input().split())
listtree=[1]*(L+1)
for i in range(1,M+1):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        listtree[j]=0
print(listtree.count(1))