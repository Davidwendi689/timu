import sys
def solve():
    s = sys.stdin.read()
    n = len(s)
    res = []
    in_str = False
    i = 0
    while i < n:
        if in_str:
            if s[i] == '\\' :
                res.append(s[i])
                if i+1<n:
                    res.append(s[i+1])
                i += 2
            elif s[i] == '"':
                res.append(s[i])
                i += 1
                in_str = False
            else:
                res.append(s[i])
                i += 1
        else:
            if s[i] == '\\':
                res.append(s[i])
                if i+1<n:
                    res.append(s[i+1])
                i += 2
            elif s[i] == '"':
                res.append(s[i])
                i += 1
                in_str = True
            elif s[i:i+2] == '/*':
                j = s.find('*/', i + 2)
                if j == -1:
                    res.append('/*')
                    i += 2
                else:
                    i = j + 2
            else:
                res.append(s[i])
                i += 1
    print("".join(res),end="")
solve()