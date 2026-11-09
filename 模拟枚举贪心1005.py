a = list(map(int, input().split()))
total = sum(a)
b = []
c = []
for d in range(10):
    if a[d] % 2 == 1:
        b.append(d)
#每两个相同的数字，取一个放到左半边
    c.extend([str(d)] * (a[d] // 2))
#出现奇数次的数字最多只能有一个
if total == 0 or len(b) > 1:
    print(-1)
elif total == 1:
    print(a.index(1))
else:
#在左半边寻找最小的非零数字
    pos = -1
    for i in range(len(c)):
        if c[i] != '0':
            pos = i
            break#多位数不能以零开头
    if pos == -1:
        print(-1)
    else:
#把最小的非零数字放到第一位
        c[0], c[pos] = c[pos], c[0]
        left = ''.join(c)
#把出现奇数次的数字放在中间
        e = str(b[0]) if b else ''
        ans = left + e + left[::-1]
        print(ans)