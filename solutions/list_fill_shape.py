# Fill inside the given shape.
#
# Input:
# [
#     ['.', '.', '0', '0', '.', '0', '0', '.', '.'],
#     ['.', '0', '.', '.', '0', '.', '.', '0', '.'],
#     ['.', '0', '.', '.', '.', '.', '.', '0', '.'],
#     ['.', '.', '0', '.', '.', '.', '0', '.', '.'],
#     ['.', '.', '.', '0', '.', '0', '.', '.', '.'],
#     ['.', '.', '.', '.', '0', '.', '.', '.', '.']
# ]
#
# Output:
# [
#     ['.', '.', '0', '0', '.', '0', '0', '.', '.'],
#     ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
#     ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
#     ['.', '.', '0', '0', '0', '0', '0', '.', '.'],
#     ['.', '.', '.', '0', '0', '0', '.', '.', '.'],
#     ['.', '.', '.', '.', '0', '.', '.', '.', '.']
# ]


def fill_shape(grid, col_index, row_index):
    height = len(grid)
    width = len(grid[0])

    def flood_fill(x, y):
        if (y < 0 or y > height) or (x < 0 or x > width):  # out of range
            return

        if grid[y][x] == '0':  # already filled
            return

        if grid[y][x] == '.':
            grid[y][x] = '0'

            flood_fill(x-1, y)  # left
            flood_fill(x+1, y)  # right
            flood_fill(x, y-1)  # up
            flood_fill(x, y+1)  # down

    flood_fill(col_index, row_index)


def pretty_print(grid):
    for row in grid:
        print("".join(row))


sample_grid = [
    ['.', '.', '0', '0', '.', '0', '0', '.', '.'],
    ['.', '0', '.', '.', '0', '.', '.', '0', '.'],
    ['.', '0', '.', '.', '.', '.', '.', '0', '.'],
    ['.', '.', '0', '.', '.', '.', '0', '.', '.'],
    ['.', '.', '.', '0', '.', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '0', '.', '.', '.', '.']
]

pretty_print(sample_grid)
print('_'*9)

fill_shape(sample_grid, 2, 1)
pretty_print(sample_grid)
