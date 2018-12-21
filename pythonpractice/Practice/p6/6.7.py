tableData = [['apples', 'oranges', 'cheeries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colwidths = [0] * len(tableData)
    spam_width = []
    spam_width1 = []
    spam_width2 = []
    for number in tableData[0]:
        spam_width.append(len(number))
    colwidths[0] = max(spam_width)
    for number1 in tableData[1]:
        spam_width1.append(len(number1))
    colwidths[1] = max(spam_width1)
    for number2 in tableData[2]:
        spam_width2.append(len(number2))
    colwidths[2] = max(spam_width2)
    print(tableData[0][0].rjust(colwidths[0]) + ' ' + tableData[1][0].rjust(colwidths[1])
          + ' ' + tableData[2][0].rjust(colwidths[2]) + '\n' + 
          tableData[0][1].rjust(colwidths[0]) + ' ' + tableData[1][1].rjust(colwidths[1])
          + ' ' + tableData[2][1].rjust(colwidths[2]) + '\n' +
           tableData[0][2].rjust(colwidths[0]) + ' ' + tableData[1][2].rjust(colwidths[1])
          + ' ' + tableData[2][2].rjust(colwidths[2]) + '\n')

printTable(tableData)


