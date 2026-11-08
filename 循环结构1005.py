while True:
    try:
        a=input().strip()
        c=int(a)
        b=c+1
        for i in range(1,b):
            print(" "*2*(b-i)+"*"*i)
        for i in range(1,b+1):
            print(" "*2*(i-1)+"*"*(b+1-i))
    except Exception:
        break