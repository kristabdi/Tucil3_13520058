from util import *
from simpul import *

# Step 1
state = "y"
while (state == 'y' or state == 'Y') :
    print("==========================================================")
    print("15 PUZZLE SOLVER BY 13520058 KRISTO")
    print("==========================================================")
    choice = input("1. Random generate puzzle\n2. Input filename\n3. Exit\nChoose (1/2/3) : ")
    if (choice == '1') :
        matrix = generateMatrix(4, 4)
    elif (choice == '2') :
        # filename = "test/gfg3.txt"
        filename = input("Input filename : ")
        matrix = inputFileMatrix(filename)
    if (choice == '1' or choice == '2') :
        sigma = kurangSigma(matrix) + isReachable(matrix)
        print(f'X = {isReachable(matrix)}')
        print(f'Sigma Kurang(i) : {sigma}')
        print("==========================================================\n")
        # Step 2
        if (sigma % 2 == 0) :
            tilekosong = getTileKosong(matrix)
            initialCost = countMisplacedTiles(matrix)
            root = [[], matrix, tilekosong, initialCost, 0, None]

            pq = PrioQueue()
            pq.push(root)
            solve(pq)
        else :
            print("Puzzle tidak bisa diselesaikan, gunakan puzzle lain!")
        # root = TreeNode(None, matrix, tilekosong, initialCost, 0, None)
        state = input("Apakah anda ingin melanjutkan (y/n) ? ")
    else :
        state = 'n'

print("======================================")
print("GOODBYE!")
print("======================================")
