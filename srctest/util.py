import random

def inputFileMatrix(filename) :
    matrix = []
    try :
        with open(filename) as f:
            for line in f:
                nums = [int(n) for n in line.split()]
                matrix.append(nums)
        printMatrix(matrix)
    except  :
        print("File tidak ditemukan! Silahkan ulangi kembali!")
        return "-"
    return matrix

def generateMatrix() :
    matrix = []
    choices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    for i in range(4):  
        arr = []
        for j in range(4):
            val = random.choice(choices)
            arr.append(val)
            choices.remove(val)
        matrix.append(arr)
    printMatrix(matrix)
    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            print("%d " % (matrix[i][j]), end = " ")
        print()

def unflattenMatrix(matrix) :
    _matrix = [[-999 for i in range(4)] for i in range(4)]
    x = 0
    for i in range(4) :
        for j in range(4) :
            _matrix[i][j] = matrix[x]
            x += 1
    return _matrix

def flattenMatrix(matrix) :
    _matrix = [-999 for i in range(16)]
    x = 0
    for i in range(4) :
        for j in range(4) :
            _matrix[x] = matrix[i][j]
            x += 1
    return _matrix

def hashed(matrix):
    res = ""
    symbol = "aBCdEFgHI,;[.]/']?`~!@#$%^&*()_+-=<>|:"
    for element in matrix:
        res += symbol[element]
    return res

def isReachable(matrix) :
    solution = [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            if (solution[i][j] == 1) and (matrix[i][j] == 16) :
                return 1
    return 0

def isSolution(matrix) :
    return (countMisplacedTiles(matrix) == 0)

def kurang(matrix, row, col, kurangList) :
    res = 0
    for i in range(row, len(matrix)) :
        start = col if (i == row) else 0
        for j in range(start, len(matrix[i])) :
            if (row == i and col == j) : continue
            if (matrix[row][col] > matrix[i][j]) :
                res += 1

    kurangList.append([matrix[row][col], res])
    return res

def kurangSigma(matrix) :
    res = 0
    kurangList = []
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            res += kurang(matrix, i, j, kurangList)
    kurangList = sorted(kurangList,key=lambda x: (x[0]))
    for i in range(len(kurangList)) :
        print(f'Kurang({kurangList[i][0]}) = {kurangList[i][1]}')
    return res

def countMisplacedTiles(matrix):
    solution = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if ((matrix[i][j]) and
                (matrix[i][j] != solution[i][j])):
                count += 1
    return count

def getTileKosong(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 16:
                return [i, j]