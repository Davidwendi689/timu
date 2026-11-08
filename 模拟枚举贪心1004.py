mp = {"zero": "0", "two": "2", "four": "4", "six": "6", "nine": "9"}

t = int(input())
for _ in range(t):
    s = input().strip()
    res = []
    i = 0
    while i < len(s):
        if s[i] in "02469":
            res.append(s[i])
            i += 1
        elif s[i:i + 4] in mp:
            res.append(mp[s[i:i + 4]])
            i += 4
        elif s[i:i + 3] in mp:
            res.append(mp[s[i:i + 3]])
            i += 3
        else:
            i += 1
    print(''.join(res))