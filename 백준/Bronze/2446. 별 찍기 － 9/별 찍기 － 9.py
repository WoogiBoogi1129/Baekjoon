def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    total_rows = 2 * N - 1

    out_lines = []
    for i in range(1, total_rows + 1):
        if i <= N:
            stars = 2 * (N - i) + 1
            indent = i - 1
        else:
            # for rows N+1 .. 2N-1
            # mirror of the above
            mirror_i = total_rows - i + 1
            stars = 2 * (N - mirror_i) + 1
            indent = mirror_i - 1

        line = ' ' * indent + '*' * stars
        out_lines.append(line)

    sys.stdout.write('\n'.join(out_lines))


if __name__ == "__main__":
    main()
