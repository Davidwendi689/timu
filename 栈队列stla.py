a=[]
b=[False]*9
def rosy():    
    if len(a)==8:
        print(*a)
        return
    for i in range(1,9):
        if b[i]==False:
            a.append(i)
            b[i]=True
            rosy()
            a.pop()
            b[i]=False
rosy()            
#这个真的是很好地dsh题每一层的rosy负责一个排列的位数还有多个for的嵌套        