a=input()
b=ord(a)
c=b-64
for i in range(1,c+1):
    print(" "*(c-i),end="")
    for j in range(65,65+i):
        print(chr(j),end="")
    for y in range(63+i,64,-1):
        print(chr(y),end="")
    print()    