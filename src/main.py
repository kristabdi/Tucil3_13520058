import time
from node import *

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

if __name__ == "__main__":
    main()