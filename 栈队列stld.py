n=int(input())
a=input().split()
for i in range(0,n):
    for j in range(n-1-i):
        if a[j]+a[j+1]<a[j+1]+a[j]:
            a[j],a[j+1]=a[j+1],a[j]
print("".join(a))