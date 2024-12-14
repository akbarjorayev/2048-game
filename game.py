import tkinter as tk
import app

root = tk.Tk()
root_min_size = 400
root.title("2048 Game")
root.minsize(root_min_size, root_min_size)

app.get_board(root)
app.get_buttons(root)

root.mainloop()
