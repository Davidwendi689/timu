T=int(input())
for i in range(1,T+1):
    a=int(input())
    b=list(map(int,input().split()))
    jicha=(max(b)-min(b))
    c=sum(b)
    d=c/a
    e=[x-d for x in b]
    f=[x**2 for x in e]
    fangcha=(sum(f)/a) 
    print(f"{jicha} {fangcha:.3f}")