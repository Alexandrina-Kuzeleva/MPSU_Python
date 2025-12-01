s = input().strip()
col = ord(s[0]) - ord('a')
row = int(s[1]) - 1             

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

board = [['.' for _ in range(8)] for _ in range(8)]
board[row][col] = 'K'

for dr, dc in moves:
    nr = row + dr
    nc = col + dc
    if 0 <= nr < 8 and 0 <= nc < 8:
        board[nr][nc] = '*'

for i in range(7, -1, -1):
    print(' '.join(board[i]))