import tkinter as tk
def on_click(button_value):
    current = entry.get()

    if button_value == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_value == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, str(button_value))

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=20, font=("Arial", 20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=30, pady=30, font=("Arial", 16), command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, sticky="nsew")

for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

for child in window.winfo_children():
    child.grid_configure(padx=5, pady=5)

footer_label = tk.Label(window, text="Calculator", font=("Arial", 10) ,foreground="#265073", pady=10)
footer_label.grid(row=5, column=0, columnspan=4)

window.mainloop()