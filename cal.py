import tkinter as tk

# -----------------------------
# Calculator Logic
# -----------------------------
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))


def clear_entry():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# -----------------------------
# GUI Setup
# -----------------------------
window = tk.Tk()
window.title("GUI Calculator")
window.geometry("300x400")
window.resizable(False, False)

entry = tk.Entry(
    window,
    font=("Arial", 20),
    borderwidth=5,
    relief="ridge",
    justify="right"
)
entry.pack(fill="both", padx=10, pady=10)

# -----------------------------
# Buttons
# -----------------------------
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)
]

frame = tk.Frame(window)
frame.pack(expand=True, fill="both")

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            frame, text=text, font=("Arial", 14),
            command=calculate
        )
    else:
        btn = tk.Button(
            frame, text=text, font=("Arial", 14),
            command=lambda t=text: button_click(t)
        )

    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Clear button
clear_btn = tk.Button(
    window, text="Clear", font=("Arial", 14),
    command=clear_entry
)
clear_btn.pack(fill="both", padx=10, pady=5)

# Make buttons expand evenly
for i in range(5):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

window.mainloop()
