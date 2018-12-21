grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def set_grid(grid):
    final = ''
    for y in range(0,len(grid[0])):
        for x in range(0,len(grid)):
            if x < len(grid)-1:
                final += grid[x][y]
            else:
                final += grid[x][y] + '\n'
    return(final)
        
result = set_grid(grid)
print(result)
    


            



