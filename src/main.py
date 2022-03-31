from heapq import heappop, heappush
import time
from inout import *
from util import *

def main() :
    state = "y"
    while (state == 'y' or state == 'Y') :
        print("==========================================================")
        print("            15 PUZZLE SOLVER BY 13520058 KRISTO           ")
        print("==========================================================")
        print("Menu : ")
        choice = input("1. Random generate puzzle\n2. Input filename\n3. Exit\nChoose (1/2/3) : ")
        if (choice == '1') :
            matrix = generateMatrix()
        elif (choice == '2') :
            print()
            print("Input Filename Testcase Formatting : <namafile>.txt")
            filename = "test/" + input("Input filename (example: test.txt): ")
            matrix = inputFileMatrix(filename)
            if (matrix == "-") : exit()
        
        if (choice == '1' or choice == '2') :
            sigma = kurangSigma(matrix) + isReachable(matrix)
            print(f'X = {isReachable(matrix)}')
            print(f'Sigma Kurang(i) : {sigma}')
            print("==========================================================", end="")
            # Step 2
            if (sigma % 2 == 0) :
                now = time.time()
                puzzle = Puzzle()
                puzzle.solve(matrix)
                print(f'Elapsed execution time : {time.time()-now} seconds.')
            else :
                print("Puzzle can't be solved, use another puzzle!")
            # root = TreeNode(None, matrix, tilekosong, initialCost, 0, None)
            state = input("Do you want to continue (y/n) ? ")
        else :
            break

    print("======================================")
    print("               GOODBYE!               ")
    print("======================================")

class PrioQueue:
    def __init__(self):
        self.heap = []
    # Insert new element
    def push(self, k):
        heappush(self.heap, k)
    # Remove minimum element
    def pop(self):
        return heappop(self.heap)
    # Check if the Queue is empty
    def isEmpty(self):
        if not self.heap:
            return True
        else:
            return False

class Puzzle :
    def __init__(self) :
        self.tracker = {}
        self.linkedList = {}
        self.costDict = {}
        self.parentDict = {}
        self.depthDict = {}

    def solve(self, initialMatrix) :
        key = self.initialize(initialMatrix)
        count_simpul, idxGoal = self.branchAndBound(initialMatrix, key)
        self.printPathSolution(count_simpul, idxGoal)

    def branchAndBound(self, initialMatrix, key) :
        # Create Priority Queue        
        pq = PrioQueue()
        pq.push((self.costDict[key], key))
        found = False

        while ((not pq.isEmpty()) and (not found)):
            cost, nodeIdx = pq.pop()

            explore = self.linkedList[nodeIdx]
            # Create child, move empty tile goes up, down, left, right if valid
            if (isSolution(explore)):
                # F.S. key is the index of the goal state
                found = True
                break

            directionMatrix = getDirectionList(explore)
            for matrix in directionMatrix:
                if (matrix == -1):
                    # Move is invalid (kena ujung)
                    continue
                
                shorted = hashed(flattenMatrix(matrix))
                if (shorted in self.tracker):
                    # Continue if state of matrix already visited
                    continue

                # New node
                key += 1
                # Add to tracker every time a state of matrix visited
                self.tracker[shorted] = 1 
                # Add to linked list to store matrix
                self.linkedList[key] = matrix
                # Cost Function
                self.depthDict[key] = self.depthDict[nodeIdx] + 1
                self.costDict[key] = countMisplacedTiles(matrix) + self.depthDict[key]
                # Add index to dict of parent index
                self.parentDict[key] = nodeIdx
                if (isSolution(matrix)):
                    # F.S. key is the index of the goal state
                    found = True
                    break
                pq.push((self.costDict[key], key))

        count_simpul = key
        return count_simpul, key

    def printPathSolution(self, count_simpul, key) :
        path = key
        solution = []
        done = False
        while (not done):
            solution.append(path)
            if (path == 1): done = True
            # Get linked to parent of each node
            path = self.parentDict[path]
        solution = solution[::-1]
        listOfMatrixRootToGoal = {}
        for i in range(len(solution)):
            listOfMatrixRootToGoal[i] = self.linkedList[solution[i]]

        for i in range(len(listOfMatrixRootToGoal)):
            # Print from root to goal state
            print()
            print()
            printMatrix(listOfMatrixRootToGoal[i])
        print(f'\nRaised nodes : {count_simpul}')

        # initialMtrix, return key
    def initialize(self, initialMatrix) :
        # Create initial node for hashing in dict 
        shorted = hashed(flattenMatrix(initialMatrix))
        key = 1
        # Create Dictionary
        # To contain dictionary with hashed matrix as key and number as a value
        self.tracker[shorted] = 1
        # To contain dictionary with number as key point to a matrix
        self.linkedList[1] = initialMatrix
        # To contain depth and cost of each node
        self.costDict[key] = countMisplacedTiles(initialMatrix)
        # To contain list of parent of each node
        self.parentDict[key] = key
        # To store depth of each node
        self.depthDict[key] = 0

        return key

if __name__ == "__main__":
    main()