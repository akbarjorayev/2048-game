import app
import moves


def move_keyboard(event):
    key_data = [
        {"keys": ["Up", "w"], "function": moves.move_up},
        {"keys": ["Down", "s"], "function": moves.move_down},
        {"keys": ["Left", "a"], "function": moves.move_left},
        {"keys": ["Right", "d"], "function": moves.move_right},
    ]

    for data in key_data:
        if event.keysym in data["keys"] or event.keysym.lower() in data["keys"]:
            app.update_board(data["function"])
            break
