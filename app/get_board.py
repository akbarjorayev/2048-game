import tkinter as tk
from tkinter import ttk
import board

random_cords = board.get_random_cords.two()
for cord in random_cords:
    board.board[cord[0]][cord[1]] = 2

labels = []


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
            box = tk.Label(
                frame,
                bg="gray",
                fg="white",
                relief="ridge",
                borderwidth=1,
                text=str(board.board[row][col]),
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
            labels[row][col].config(text=str(board.board[row][col]))
