ci=[]
n,k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(0,n):
    c=(A[i]-B[i])
    ci.append(c)
ci.sort(reverse=True)
d=sum(B)
for i in range(0,k):
    d+=ci[i]  
print(d)