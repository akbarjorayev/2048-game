from board import board


def move_down():
    for j in range(len(board[0])):
        new_column = [board[i][j] for i in range(len(board)) if board[i][j] != 0]
        merged_column = []

        i = len(new_column) - 1
        while i > 0:
            if new_column[i] == new_column[i - 1]:
                merged_column.append(new_column[i] * 2)
                i -= 1
            else:
                merged_column.append(new_column[i])
            i -= 1

        if i == 0:
            merged_column.append(new_column[i])

        merged_column = [0] * (len(board) - len(merged_column)) + merged_column

        for i in range(len(board)):
            board[i][j] = merged_column[i]

    return board
