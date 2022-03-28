def inputFileMatrix(filename) :
    matrix = []
    with open(filename) as f:
        for line in f:
            matrix.append(line.split())
    print(matrix)
    return matrix

def inputMatrix(row, column) :
    matrix = []
    for i in range(row):       # A outer for loop for row entries   
        inputRow =[]   
        for j in range(column):     # A inner for loop for column entries   
            inputRow.append(input()) # Take input by endline
        matrix.append(inputRow)
    return matrix