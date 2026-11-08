n = int(input())
a = list(map(int, input().split()))
a.sort()
found = False
for i in range(n - 2):
    x = a[i]
    y = a[i + 1]
    z = a[i + 2]
    if x + y > z:
        print(x, y, z)
        found = True
        break
if not found:
    print("No solution")