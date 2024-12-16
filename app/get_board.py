import tkinter as tk
from tkinter import ttk
import board

random_cords = board.get_random_cords.two()
for cord in random_cords:
    board.board[cord[0]][cord[1]] = 2

labels = []

colors = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
}


def get_board(root):
    global labels

    window_size = 500
    root.configure(bg="black")
    root.geometry(f"{window_size}x{window_size}")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TButton",
        font=("Segoe UI", 10),
        padding=5,
        background="gray",
        foreground="white",
    )

    box_size = 300
    frame = tk.Frame(root, width=box_size, height=box_size, bg="black")
    frame.place(relx=0.5, rely=0.5, anchor="center")
    frame.grid_propagate(False)

    box_pixel_size = box_size / 4
    for row in range(4):
        row_labels = []
        for col in range(4):
            value = board.board[row][col]
            box = tk.Label(
                frame,
                bg=colors.get(value, "gray"),
                fg="black" if value in (2, 4) else "white",
                relief="ridge",
                borderwidth=1,
                text=str(value) if value != 0 else "",
                font=("Segoe UI", 20),
            )
            box.place(
                x=col * box_pixel_size,
                y=row * box_pixel_size,
                width=box_pixel_size,
                height=box_pixel_size,
            )
            row_labels.append(box)
        labels.append(row_labels)


def update_board(move):
    board.board = move()

    blank_cords = board.get_blank()
    board.board[blank_cords[0]][blank_cords[1]] = 2

    for row in range(4):
        for col in range(4):
            value = board.board[row][col]
            labels[row][col].config(
                text=str(value) if value != 0 else "",
                bg=colors.get(value, "gray"),
                fg="black" if value in (2, 4) else "white",
            )
