def matrix_multiply(matrix1, matrix2):
    # mendapatkan dimensi dari matriks
    m1_rows, m1_cols = len(matrix1), len(matrix1[0])
    m2_rows, m2_cols = len(matrix2), len(matrix2[0])

    # cek jika metrik dapat dikalikan
    if m1_cols != m2_rows:
        return "Error: The number of columns in the first matrix must be equal to the number of rows in the second matrix."

    # membuat matriks hasil dengan nol
    result = [[0 for _ in range(m2_cols)] for _ in range(m1_rows)]

    # lakukakn perkalian
    for i in range(m1_rows):
        for j in range(m2_cols):
            for k in range(m1_cols):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Test fungsi dengan dua matriks
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
result = matrix_multiply(matrix1, matrix2)
for row in result:
    print(row)
