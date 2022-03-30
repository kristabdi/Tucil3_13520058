from heapq import heappop, heappush
import _pickle as cPickle
import time
from util import *

# Step 1
def main() :
    state = "y"
    while (state == 'y' or state == 'Y') :
        print("==========================================================")
        print("15 PUZZLE SOLVER BY 13520058 KRISTO")
        print("==========================================================")
        choice = input("1. Random generate puzzle\n2. Input filename\n3. Exit\nChoose (1/2/3) : ")
        if (choice == '1') :
            matrix = generateMatrix()
        elif (choice == '2') :
            print("Masukkan filename tes uji dengan format <namafile>.txt")
            filename = "test/" + input("Input filename (contoh: test.txt): ")
            matrix = inputFileMatrix(filename)
            if (matrix == "-") : exit()
        
        if (choice == '1' or choice == '2') :
            sigma = kurangSigma(matrix) + isReachable(matrix)
            print(f'X = {isReachable(matrix)}')
            print(f'Sigma Kurang(i) : {sigma}')
            print("==========================================================\n")
            # Step 2
            if (sigma % 2 == 0) :
                now = time.time()
                puzzle = Puzzle()
                puzzle.solve(flattenMatrix(matrix))
                print(f'Waktu yang dibutuhkan untuk menyelesaikan puzzle : {time.time()-now} detik.')
            else :
                print("Puzzle tidak bisa diselesaikan, gunakan puzzle lain!")
            # root = TreeNode(None, matrix, tilekosong, initialCost, 0, None)
            state = input("Apakah anda ingin melanjutkan (y/n) ? ")
        else :
            break

    print("======================================")
    print("GOODBYE!")
    print("======================================")



def move(matrix, idx, direction):
    res = cPickle.loads(cPickle.dumps(matrix, -1))
    if (direction == 0):
        if ((idx // 4) > 0) :
            res[idx], res[idx - 4] = res[idx - 4], res[idx]
            return res
        else :
            return -1
    elif (direction == 1):
        if ((idx // 4) < 3):
            res[idx + 4], res[idx] = res[idx], res[idx + 4]
            return res
        else:
            return -1
    elif (direction == 2):
        if (idx % 4 > 0):
            res[idx - 1], res[idx] = res[idx], res[idx - 1]
            return res
        else:
            return -1
    else :
        if (idx % 4 < 3):
            res[idx], res[idx + 1] = res[idx + 1], res[idx]
            return res
        else:
            return -1

class Puzzle :
    def __init__(self) :
        self.tracker = {}
        self.linkedList = {}
        self.costDict = {}
        self.parentDict = {}
        self.depthDict = {}
        
    def solve(self, initialMatrix) :
        # Create initial node for hashing in dict 
        hashedMatrix = hashed(initialMatrix)
        indexing = 1
        # Create Dictionary
        # To contain dictionary with hashed matrix as key and number as a value
        self.tracker[hashedMatrix] = 1
        # To contain dictionary with number as key point to a matrix
        self.linkedList[1] = initialMatrix
        # To contain depth and cost of each node
        self.costDict[indexing] = 0 
        # To contain list of parent of each node
        self.parentDict[indexing] = indexing
        # To store depth of each node
        self.depthDict[indexing] = 0

        # Initialization
        pq = [(self.costDict[indexing], indexing)]
        
        found = False

        while ((pq) and (not found)):
            cost, nodeIdx = heappop(pq)

            root = self.linkedList[nodeIdx]
            tilekosong = getTileKosong(root)

            # Create child, move empty tile goes up, down, left, right if valid
            directionMatrix = []
            for i in range(4) :
                directionMatrix.append(move(root, tilekosong, i))

            for matrix in directionMatrix:
                if (matrix == -1):
                    continue
                
                hashedMatrix = hashed(matrix)
                if (hashedMatrix in self.tracker):
                    # Continue if state of matrix already visited
                    continue

                # New node
                indexing += 1
                # Add to tracker every time a state of matrix visited
                self.tracker[hashedMatrix] = 1 
                # Add to linked list to store matrix
                self.linkedList[indexing] = matrix
                # Cost Function
                self.depthDict[indexing] = self.depthDict[nodeIdx] + 1
                self.costDict[indexing] = countMisplacedTiles(unflattenMatrix(matrix)) + self.depthDict[indexing]
                # Add index to dict of parent index
                self.parentDict[indexing] = nodeIdx

                if (isSolution(unflattenMatrix(matrix))):
                    found = True
                    break

                heappush(pq, (self.costDict[indexing], indexing))


        count_simpul = indexing
        solution = []

        done = False
        while(not done):
            solution.append(indexing)
            if (indexing == 1): done = True
            # Get linked to parent of each node
            indexing = self.parentDict[indexing]

        solution = solution[::-1]
        for i in range(len(solution)):
            print(f'Langkah ke-{i+1} :')
            printFlattenedMatrix(self.linkedList[solution[i]])
        print(f'Jumlah simpul yang dibuat : {count_simpul}')

if __name__ == "__main__":
    main()