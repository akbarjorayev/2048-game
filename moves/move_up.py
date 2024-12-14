from board import board


def move_up():
    for j in range(len(board[0])):
        new_column = [board[i][j] for i in range(len(board)) if board[i][j] != 0]
        merged_column = []

        i = 0
        while i < len(new_column) - 1:
            if new_column[i] == new_column[i + 1]:
                merged_column.append(new_column[i] * 2)
                i += 1
            else:
                merged_column.append(new_column[i])
            i += 1

        if i == len(new_column) - 1:
            merged_column.append(new_column[i])

        for i in range(len(board)):
            board[i][j] = merged_column[i] if i < len(merged_column) else 0

    return board
