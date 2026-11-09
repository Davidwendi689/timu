import sys
middle = {
    "13": "2", "31": "2",
    "17": "4", "71": "4",
    "39": "6", "93": "6",
    "79": "8", "97": "8",
    "19": "5", "91": "5",
    "37": "5", "73": "5",
    "28": "5", "82": "5",
    "46": "5", "64": "5"
}
for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    used = []
    prev = ""
    good = True
    for ch in s:

        # 检查数字是否重复
        if ch in used:
            good = False
            break

        # 检查上一个数字到当前数字的连线
        if prev != "":
            key = prev + ch

            if key in middle:
                need = middle[key]

                if need not in used:
                    good = False
                    break

        # 当前数字合法，记录下来
        used.append(ch)
        prev = ch

    if good:
        print("YES")
    else:
        print("NO")