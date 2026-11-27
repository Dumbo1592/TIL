def snail(n):
    col, row, dir, cnt = 0, 0, 0, 1
    answer = [[0] * n for _ in range(n)]

    while cnt <= n*n:
        if dir == 0: # right
            while col < n and not answer[row][col]:
                answer[row][col] = cnt
                col, cnt = col + 1, cnt + 1
            dir, row, col = dir + 1, row + 1, col - 1

        elif dir == 1: # down
            while row < n and not answer[row][col]:
                answer[row][col] = cnt
                row, cnt = row + 1, cnt + 1
            dir, row, col = dir + 1, row - 1, col - 1

        elif dir == 2: # left
            while col > -1 and not answer[row][col]:
                answer[row][col] = cnt
                col, cnt = col - 1, cnt + 1
            dir, row, col = dir + 1, row - 1, col + 1

        elif dir == 3: # up
            while not answer[row][col]:
                answer[row][col] = cnt
                row, cnt = row - 1, cnt + 1
            dir, row, col = 0, row + 1, col + 1

    for i in range(n):
        for j in range(n):
            if j < n-1:
                print(f"{answer[i][j]} ", end="")
            else:
                print(f"{answer[i][j]}")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    data = [0 for _ in range(n * n)]
    print(f"#{test_case}")
    snail(n)
        
# ///////////////////////////////////////////////////////////////////////////////////