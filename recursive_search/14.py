def n_queens(n):
    def dfs(row, cols, diag1, diag2):
        if row == n:
            return 1
        total = 0
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if cols[col] or diag1[d1] or diag2[d2]:
                continue
            cols[col] = diag1[d1] = diag2[d2] = True
            total += dfs(row + 1, cols, diag1, diag2)
            cols[col] = diag1[d1] = diag2[d2] = False
        return total

    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    return dfs(0, cols, diag1, diag2)


n = int(input())
print(n_queens(n))