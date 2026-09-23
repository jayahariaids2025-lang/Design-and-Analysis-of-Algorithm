def is_safe(board, row, col):
for prev_row in range(row):
placed = board[prev_row]
if placed == col: # Same column
return False
if abs(prev_row - row) == abs(placed - col): # Diagonal
return False
return True
def solve_n_queens(n):
board = [-1] * n
solutions = []
backtrack_count = [0]
def backtrack(row):
if row == n:
solutions.append(board[:])
return
for col in range(n):
if is_safe(board, row, col):
board[row] = col
backtrack(row + 1)
board[row] = -1 # Undo
backtrack_count[0] += 1
backtrack(0)
return solutions, backtrack_count[0]
def display_board(solution, n):
print(&#39; +&#39; + &#39;---+&#39; * n)
for row in range(n):
print(&#39; |&#39;, end=&#39;&#39;)
for col in range(n):
if solution[row] == col:
print(&#39; Q |&#39;, end=&#39;&#39;)
else:
print(&#39; . |&#39;, end=&#39;&#39;)
print()
print(&#39; +&#39; + &#39;---+&#39; * n)
# --- Solve for N=4 (show all) and N=8 (count only) ---
for n in [4, 6, 8]:
solutions, backtracks = solve_n_queens(n)
print(f&#39;N={n}: {len(solutions)} solutions, {backtracks} backtracks&#39;)
if n == 4:
print(f&#39;\n All solutions for {n}-Queens:&#39;)
for i, sol in enumerate(solutions, 1):
print(f&#39;\n Solution {i}: {sol}&#39;)
display_board(sol, n)
