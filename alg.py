# class Search:
#     nums = [8,8, 8,9,10]
#
#     def __init__(self, target):
#         self.target = target
#
#     def search_position(self):
#         index = 0
#         result = []
#         for i in self.nums:
#             if i == self.target:
#                 result.append(index)
#             index += 1
#         if result == []:
#             result.append('-1,-1')
#         return f'{self.nums}, target = {self.target}, Output: {result}'
# pos1 = Search(8)
# print(pos1.search_position())

# def spiralOrder(matrix):
#     # Результат будет хранится здесь.
#     result = []
#     # Пока в нашей матрице ещё есть строки...
#     while matrix:
#         # Добавьте первую строку в результат и удалите её из матрицы.
#         result += matrix.pop(0)
#         # Если в матрице ещё остались строки...
#         if matrix and matrix[0]:
#             # Добавьте последний элемент каждой оставшейся строки в результат и удалите его из строки.
#             for row in matrix:
#                 if row:
#                     result.append(row.pop())
#             # Если в матрице ещё остались строки после удаления...
#             if matrix and matrix[-1]:
#                 # Добавьте последнюю строку в обратном порядке в результат и удалите её из матрицы.
#                 result += matrix.pop()[::-1]
#                 # Если в матрице ещё остались строки...
#                 if matrix and matrix[0]:
#                     # Добавьте первый элемент каждой оставшейся строки в обратном порядке в результат и удалите его из строки.
#                     for row in matrix[::-1]:
#                         if row:
#                             result.append(row.pop(0))
#
#     return result
#
#
# matrix = [[1,2,3],[4,5,6],[7,4,5],[10,11,12], [1,2,3], [23,3,5], [2,4,6]]
# print(spiralOrder(matrix))


def is_valid_sudoku(board):
    # Проверка каждой строки
    for row in board:
        if not is_valid_row(row):
            return False

    # Проверка каждого столбца
    for col in range(len(board[0])):
        column = []
        for row in range(len(board)):
            column.append(board[row][col])
        if not is_valid_row(column):
            return False

    # Проверка каждого подполя 3х3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = []
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    subgrid.append(board[row][col])
            if not is_valid_row(subgrid):
                return False

    return True


def is_valid_row(row):
    # Проверка, содержит ли строка только цифры от 1 до 9 без повторений
    digits = set()
    for num in row:
        if num != ".":
            if num in digits:
                return False
            digits.add(num)
    return True


# Пример доски для судоку
board = [
    ["5", "3", "", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

if is_valid_sudoku(board):
    print("Доска для судоку действительна.")
else:
    print("Доска для судоку недействительна.")