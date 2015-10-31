global errorMessage
global testSudoku
errorMessage = "Input was not a proper sudoku puzzle"
originalTestSudoku = [[5,0,0,0,9,1,0,0,8],
                      [0,0,0,0,0,3,0,2,0],
                      [0,0,3,0,0,0,5,0,0],
                      [0,0,9,0,8,2,0,4,0],
                      [0,4,0,1,0,6,0,9,0],
                      [0,6,0,9,4,0,3,0,0],
                      [0,0,6,0,0,0,7,0,0],
                      [0,7,0,3,0,0,0,0,0],
                      [3,0,0,5,2,0,0,0,4]]

test = [[5,0,7,6,9,1,0,3,8],
        [6,0,0,0,5,3,0,2,7],
        [0,0,3,0,7,0,5,0,6],
        [0,3,9,7,8,2,6,4,5],
        [7,4,5,1,3,6,8,9,2],
        [0,6,0,9,4,5,3,7,0],
        [0,5,6,0,1,0,7,0,3],
        [0,7,0,3,6,0,0,5,0],
        [3,0,0,5,2,7,0,6,4]]

testSudoku = [[0,0,6,0,0,8,5,0,0],
              [0,0,0,0,7,0,6,1,3],
              [0,0,0,0,0,0,0,0,9],
              [0,0,0,0,9,0,0,0,1],
              [0,0,1,0,0,0,8,0,0],
              [4,0,0,5,3,0,0,0,0],
              [1,0,7,0,5,3,0,0,0],
              [0,5,0,0,6,4,0,0,0],
              [3,0,0,1,0,0,0,6,0]]
              

def sudokuSolver(sudoku):
    """
    Main function that calls helper functions so find an
    a solution to the given sudoku puzzle, sudoku.
    """

    s = sudoku

    #find the cells that need to be modified
    cellsToFill = []
    i = 0
    j = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i][j] == 0:
                cellsToFill.append([i, j])

    #loop through all empty cells and try each possible input
    i = 0
    while i < len(cellsToFill):
        if i < 0:
            return "Cannot solve the sudoku puzzle"
        row = cellsToFill[i][0]
        column = cellsToFill[i][1]
        if s[row][column] == 9:
            s[row][column] = 0
            i -= 2
        else:
            s[row][column] += 1
            while s[row][column] < 10:
                if checkValid(s):
                    break
                #if after going through all possible inputs, you can't find
                #a number that fits, go back to the previous empty cell
                if s[row][column] == 9:
                    s[row][column] = 0
                    i -= 2
                    break
                s[row][column] += 1
        i += 1
    return s
    

def checkValid(sudoku):
    """
    Check if sudoku sudoku is valid.
    Look for repeats in all rows, columns, and 3x3 boxes.
    """
    
    if len(sudoku) != 9:
        return False

    for i in range(len(sudoku)):
        if not checkRow(sudoku[i]):
            return False
        if not checkColumn(sudoku, i):
            return False

    boxes = intoThirds(sudoku)
    for i in range(len(boxes)):
        if not checkRow(boxes[i]):
            return False
            
    return True


def createColumn(sudoku, columnIndex):
    """
    Because the puzzle is input as a nested array, based on columnIndex,
    create the column for that columnIndex.
    """

    column = []
    i = 0
    for i in range(len(sudoku)):
        column += [sudoku[i][columnIndex]]
    return column


def checkColumn(sudoku, columnIndex):
    """
    For sudoku sudoku, check if the given column at columnIndex has
    any repeated values within the column.
    """

    column = createColumn(sudoku, columnIndex)
    if len(column) != 9:
        return False
    currentValues = []
    for i in range(len(column)):
        if column[i] != 0:
            if column[i] not in range(0, 10):
                return False
            if column[i] not in currentValues:
                currentValues += [column[i]]
            else:
                return False
    return True


def checkRow(row):
    """
    For the given row, of a sudoku, check if the row as any repeated
    values.
    """

    if len(row) != 9:
        return False
    currentValues = []
    for i in range(len(row)):
        if row[i] != 0:
            if row[i] not in range(0, 10):
                return False
            if row[i] not in currentValues:
                currentValues += [row[i]]
            else:
                return False
    return True


def intoThirds(sudoku):
    """
    For sudoku sudoku, check hold all values within each 3x3 box
    in an array.
    """

    rowStart = 0
    rowEnd = 3
    columnStart = 0
    columnEnd = 3
    boxes = [[],[],[],[],[],[],[],[],[]]

    for k in range(len(boxes)):
        for i in range(rowStart, rowEnd):
            for j in range(columnStart, columnEnd):
                boxes[k] += [sudoku[i][j]]
        if k == 2:
            rowStart = 0
            rowEnd = 3
            columnStart += 3
            columnEnd += 3
        elif k == 5:
            rowStart = 0
            rowEnd = 3
            columnStart += 3
            columnEnd += 3
        else:
            rowStart += 3
            rowEnd += 3
    return boxes
        

                
if __name__ == "__main__":
    print(sudokuSolver(testSudoku))
