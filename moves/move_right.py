from board import board


def move_right():
    for i in range(len(board)):
        new_row = [tile for tile in board[i] if tile != 0]
        merged_row = []

        j = len(new_row) - 1
        while j > 0:
            if new_row[j] == new_row[j - 1]:
                merged_row.append(new_row[j] * 2)
                j -= 1
            else:
                merged_row.append(new_row[j])
            j -= 1

        if j == 0:
            merged_row.append(new_row[0])

        merged_row = [0] * (len(board[i]) - len(merged_row)) + merged_row

        board[i] = merged_row

    return board
