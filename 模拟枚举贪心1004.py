t=int(input())
a="02469"
b={"zero":"0","two":"2","four":"4","six":"6","nine":"9"}
for _ in range(t):
    c=[]
    s=input().strip()
    i=0
    while i < len(s):
        if s[i] in a:
            c+=(s[i])
            i+=1
            continue
        d=False
        for z,e in b.items():
            if s.startswith(z,i):
                c+=(e) 
                i+=len(z)
                d=True
                break
        if not d:
            i+=1
    print("".join(c))
#原来这道验证码这样做那还可以