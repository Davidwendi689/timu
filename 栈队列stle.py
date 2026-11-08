word=input()
b=0
good=True
if word.count("a")!=word.count("b"):
    good=False
if len(word)%2==1:
    good=False
for i in word:
    if i=="a":
        b+=1
    elif i=="b":
        b-=1
    else:
        good=False
        break
    if b<0:
        good=False
        break
if b!=0:
    good=False
if good and b==0:
    print("Good")
else:
    print("Bad")