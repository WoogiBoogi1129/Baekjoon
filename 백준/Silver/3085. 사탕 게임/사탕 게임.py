def check(board, n):
    max_count = 1

    # 행 기준 검사
    for i in range(n):
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    # 열 기준 검사
    for j in range(n):
        count = 1
        for i in range(1, n):
            if board[i][j] == board[i - 1][j]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    return max_count

def solve(board, n):
    result = 0

    for i in range(n):
        for j in range(n):
            # 오른쪽 교환
            if j + 1 < n:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                result = max(result, check(board, n))
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 원상복구

            # 아래쪽 교환
            if i + 1 < n:
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                result = max(result, check(board, n))
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]  # 원상복구

    return result

# 입력
n = int(input())
board = [list(input().strip()) for _ in range(n)]

# 결과 출력
print(solve(board, n))