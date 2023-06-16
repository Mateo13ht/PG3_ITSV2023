def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Inicializar los índices para la búsqueda
    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
target = 9

result = search_matrix(matrix, target)
print(result)  # True
