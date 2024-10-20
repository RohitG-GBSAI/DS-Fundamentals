def readNames(filename, names_list):
    with open(filename, 'r') as file:
        for line in file:
            names = line.strip().split(',')
            for name in names:
                names_list.append(name)

def loadInMatrix(names_list):
    matrix = []
    for name in names_list:
        matrix.append(name)
    return matrix

def convertToColumnMajor(matrix):
    cmatrix = matrix
    temp = []
    n = max([len(i) for i in cmatrix])
    for i in range(n):
        res = ""
        for j in range(len(cmatrix)):
            try:
                res += cmatrix[j][i]
            except Exception as e:
                res += " "
        temp.append(res)
    cmatrix.clear()
    cmatrix.extend(temp)
    print(cmatrix)

def calculateCharacterLength(matrix):
    total_length = 0
    for name in matrix:
        total_length += len(name)
    print(total_length)

def storeListAsString(matrix, output_file):
    with open(output_file, 'w') as file:
        concatenated_string = ''.join([''.join(row) for row in matrix])
        file.write(concatenated_string)

def Main():
    names_list = []
    filename = 'Namelist.csv'
    readNames(filename, names_list)  # 1
    matrix = loadInMatrix(names_list)  # 2
    convertToColumnMajor(matrix)  # 3
    calculateCharacterLength(matrix)  # 4
    output_file = 'output.txt'
    storeListAsString(matrix, output_file)  # 5
    print("Matrix:")
    for row in matrix:
        print(row)
    print(f"\nStored matrix as strings in '{output_file}'")

Main()