import _pickle as cPickle

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