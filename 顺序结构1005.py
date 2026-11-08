for i in range(1,10):
    for j in range(1,i+1):
        x=j*i
        if x<10 :
            print(f"{j}*{i}= {x}",end=" ")
        else :
            print(f"{j}*{i}={x}",end=" ")
    print()