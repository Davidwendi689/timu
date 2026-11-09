import sys
s = sys.stdin.read()
n = len(s)
i = 0
#a是状态（0 普通、1 字符串、2 注释）b表示保存输出c记录注释起点。
a = 0
b = []
c = -1
while i < n:
    if a == 0:
#转义的双引号原样保留，不转类型或者说状态
        if s[i] == '\\' and i < n - 1 and s[i + 1] == '"':
            b.append(s[i])
            b.append(s[i + 1])
            i += 2
            continue
        elif s[i] == '"':
            b.append(s[i])
            a = 1
        elif s[i] == '/' and i < n - 1 and s[i + 1] == '*':
            a = 2
            c = i
            i += 2
            continue
        else:
            b.append(s[i])
    elif a == 1:
        if s[i] == '\\' and i < n - 1 and s[i + 1] == '"':
            b.append(s[i])
            b.append(s[i + 1])
            i += 2
            continue
        elif s[i] == '"':
            b.append(s[i])
            a = 0
        else:
            b.append(s[i])
    elif a == 2:
        if s[i] == '*' and i < n - 1 and s[i + 1] == '/':
            a = 0
            c = -1
            i += 2
            continue
    i += 1
# 未闭合的注释从开始到结束样保留。
if a == 2:
    b.append(s[c:])

sys.stdout.write(''.join(b))