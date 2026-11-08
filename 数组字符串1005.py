t=int(input())
list_1=list(map(int,input().split()))
if list_1[t-1]==15:
    print("DOWN")
elif list_1[t-1]==0:
    print("UP")
elif t==1:
    print("-1")
elif list_1[-2]>list_1[-1]:
    print("DOWN")
else:
    print("UP")