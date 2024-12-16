import tkinter as tk
from tkinter import ttk
import moves
import app


def get_buttons(root):
    button_frame = tk.Frame(root, bg="black")
    button_frame.place(relx=0.5, rely=1.0, anchor="s", y=-10)

    up_button = ttk.Button(
        button_frame,
        text="Up",
        style="TButton",
        command=lambda: app.update_board(moves.move_up),
    )
    up_button.grid(row=0, column=1, padx=5, pady=5)

    left_button = ttk.Button(
        button_frame,
        text="Left",
        style="TButton",
        command=lambda: app.update_board(moves.move_left),
    )
    left_button.grid(row=1, column=0, padx=5, pady=5)

    down_button = ttk.Button(
        button_frame,
        text="Down",
        style="TButton",
        command=lambda: app.update_board(moves.move_down),
    )
    down_button.grid(row=1, column=1, padx=5, pady=5)

    right_button = ttk.Button(
        button_frame,
        text="Right",
        style="TButton",
        command=lambda: app.update_board(moves.move_right),
    )
    right_button.grid(row=1, column=2, padx=5, pady=5)
