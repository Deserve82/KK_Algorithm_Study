sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

for i in sudoku:
    print(i)
print(sudoku)