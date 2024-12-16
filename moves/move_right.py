from board import board


def move_right():
    for i in range(len(board)):
        row = [tile for tile in board[i] if tile != 0][::-1]
        merged_row = []

        j = 0
        while j < len(row):
            if j < len(row) - 1 and row[j] == row[j + 1]:
                merged_row.append(row[j] * 2)
                j += 2
            else:
                merged_row.append(row[j])
                j += 1

        merged_row += [0] * (len(board[i]) - len(merged_row))
        board[i] = merged_row[::-1]

    return board
