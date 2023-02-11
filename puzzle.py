"""https://github.com/shevchenkopn/puzzles"""


def chech_horisontally(board: list[str]) -> bool:
    """
    Checks if numbers in the row are not repeating
    """
    for i in board:
        for j in i:
            if j.isnumeric() and i.count(j) > 1:
                return True
    return False

def validate_board(board: list[str]) -> bool:
    """
    Validates board
    >>> board = [\
"**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"]
    >>> validate_board(board)
    False
    """
    board = [[*i] for i in board]

    flipped_board = []
    for i in range(len(board)):
        line = []
        for j in board:
            line.append(j[i])
        flipped_board.append(line)

    if chech_horisontally(board) or chech_horisontally(flipped_board):
        return False

    color1 = [(4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4)]
    color2 = [(3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5)]
    color3 = [(2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
    color4 = [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)]
    color5 = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)]

    colors = [color1, color2, color3, color4, color5]

    for color in colors:
        elems = ''
        for coord in color:
            item = board[coord[0]][coord[1]]
            if item.isnumeric():
                elems += item
            if elems.count(item) > 1:
                return False
    return True
