from copy import deepcopy
def Determinant(matrix):
    det = 0
    if len(matrix) == 2:
        det = (matrix[1][1] * matrix[0][0]) - (matrix[1][0] * matrix[0][1])
    else:
        for i in range(len(matrix)):
            det += pow(-1, (2+i)) * matrix[0][i] * Determinant(smaller_matrix(matrix, i))
    return det

def smaller_matrix(matrix, row):
    matrix2 = deepcopy(matrix)
    matrix2.pop(0)
    for i in range(len(matrix2)):
        matrix2[i].pop(row)
    return matrix2

dimension = int(input("Enter the dimensions of the matrix : "))
matrix = []
for i in range(dimension):
    matrix.append([])
    for j in range(dimension):
        matrix[i].append(int(input("Enter the element at position " + str(i) + ","+ str(j) + " "))) # Main matrix input complete
determinant = Determinant(matrix)
print("The Determinant of the matrix is : ", determinant)