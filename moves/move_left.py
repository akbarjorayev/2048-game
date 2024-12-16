from board import board


def move_left():
    for i in range(len(board)):
        new_row = [tile for tile in board[i] if tile != 0]
        merged_row = []

        j = 0
        while j < len(new_row):
            if j < len(new_row) - 1 and new_row[j] == new_row[j + 1]:
                merged_row.append(new_row[j] * 2)
                j += 2
            else:
                merged_row.append(new_row[j])
                j += 1

        merged_row += [0] * (len(board[i]) - len(merged_row))

        board[i] = merged_row

    return board
