while True:
    try:
        a,b,c=map(int,input().split())
        listsmall=[4,6,9,11]
        if b in listsmall:
            count=0
            for i in range(1,31):
                count+=f"{i:02d}".count(str(c))
                count+=str(a).count(str(c))
                count+=f"{b:02d}".count(str(c))
            g=int(count)
            print(f"{g}")
        elif b ==2:
            count=0
            if a%400==0 or (a%4==0 and a%100!=0):
                for i in range(1,30):
                    count+=f"{i:02d}".count(str(c))
                    count+=str(a).count(str(c))
                    count+=f"{b:02d}".count(str(c))
                g=int(count)
                print(f"{g}")
            else:
                for i in range(1,29):
                    count+=f"{i:02d}".count(str(c))
                    count+=str(a).count(str(c))
                    count+=f"{b:02d}".count(str(c))
                g=int(count)
                print(f"{g}")
        else:
            count=0
            for i in range(1,32):
                count+=f"{i:02d}".count(str(c))
                count+=str(a).count(str(c))
                count+=f"{b:02d}".count(str(c))
            g=int(count)
            print(f"{g}")
    except Exception:
        break