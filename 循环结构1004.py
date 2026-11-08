T=int(input())
for _ in range(T):
    b=int(input())
    c=b//2+1
    for j in range(1,c+1):
        print(" "*(c-j),end="")
        print("*"*(2*j-1),end="")
        print()
    for r in range(1,c):
        print(f"{' '*r}{'*'*(b-2*r)}")