def read_matrix_from_csv(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = line.strip().split(',')
            matrix.append([int(num) for num in row])
    return matrix

def multiply_matrices(matrix1, matrix2):
    result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            sum = 0
            for k in [0, 1, 2]:
                sum += matrix1[i][k] * matrix2[k][j]
            result_matrix[i][j] = sum
    return result_matrix

def write_matrix_to_csv(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(','.join([str(num) for num in row]) + '\n')

def main():
    matrix1 = read_matrix_from_csv('matrix1.csv')
    matrix2 = read_matrix_from_csv('matrix2.csv')
    print (result_matrix)
    result_matrix = multiply_matrices(matrix1, matrix2)
    write_matrix_to_csv(result_matrix, 'result_matrix.csv')

if __name__ == '__main__':
    main()
