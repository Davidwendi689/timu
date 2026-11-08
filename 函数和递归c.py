a=input()
b=int(a)+1
for i in range(len(a)-2,-1,-1):
    a+=a[i]
for i in range(2,b):
    if int(a)%i==0:
        print("noprime")
        break
else:
    print("prime")
    