import sys

def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    cnt = (data + [0] * 10)[:10]
    total = sum(cnt)

    # 奇数个的数字
    odds = [d for d in range(10) if cnt[d] % 2 == 1]
    if len(odds) > 1:
        print(-1)
        return
    middle = str(odds[0]) if odds else ""

    # 左半边：每个数字取一半，按 0~9 排好，已经是从小到大
    left = []
    for d in range(10):
        left.extend([str(d)] * (cnt[d] // 2))

    # 只有一位数
    if total == 1:
        print(middle)
        return

    # 找左半边里第一个非零数字，换到开头
    idx = next((i for i, ch in enumerate(left) if ch != '0'), None)
    if idx is None:
        print(-1)
        return
    left[0], left[idx] = left[idx], left[0]

    left_str = ''.join(left)
    print(left_str + middle + left_str[::-1])

if __name__ == '__main__':
    solve()