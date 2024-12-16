from board import board


def move_up():
    for j in range(len(board[0])):
        new_column = [board[i][j] for i in range(len(board)) if board[i][j] != 0]
        merged_column = []

        i = 0
        while i < len(new_column):
            if i < len(new_column) - 1 and new_column[i] == new_column[i + 1]:
                merged_column.append(new_column[i] * 2)
                i += 2
            else:
                merged_column.append(new_column[i])
                i += 1

        merged_column += [0] * (len(board) - len(merged_column))

        for i in range(len(board)):
            board[i][j] = merged_column[i]

    return board
