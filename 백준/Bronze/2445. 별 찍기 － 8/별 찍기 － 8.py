def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])

    out = []
    # 위쪽 (1..N)
    for i in range(1, N+1):
        # 왼쪽 별 i개
        # 가운데 공백 2*(N-i)개
        # 오른쪽 별 i개
        out.append('*' * i + ' ' * (2*(N-i)) + '*' * i)
    # 아래쪽 (N-1..1)
    for i in range(N-1, 0, -1):
        out.append('*' * i + ' ' * (2*(N-i)) + '*' * i)

    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    main()
