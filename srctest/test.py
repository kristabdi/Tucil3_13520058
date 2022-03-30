from util import *
from puzzle import *
import time

filename = "test\ow.txt"
matrix = inputFileMatrix(filename)
pz = puzzle()
pz.matrix = matrix
sigma = kurangSigma(matrix) + isReachable(matrix)
print(f'Parity (X) = {isReachable(matrix)}')
print(f'Sigma Kurang(i) : {sigma}')

if (sigma % 2 == 0) :

    temp = cPickle.loads(cPickle.dumps(puzzle, -1))
    pz.tracker[tuple(flattenMatrix(matrix))] = "-"
    pz.solve()

    while (len(temp.path) != 1) :
        temp.printPath()
        temp.printMatrix()
        print("=================")
    print("=== END SOLVE ===")
    print("Jumlah simpul dibangkitkan : " + str(len(pz.tracker) - 1))
else :
    print("Puzzle tidak bisa diselesaikan, gunakan puzzle lain!")

