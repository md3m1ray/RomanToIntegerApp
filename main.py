import tkinter as tk

"""
1	I
5	V
10	X
50	L
100	C
500	D
1000	M
5000	V̅ (Üzeri çizgili V)
"""


def convert_integer():
    pass


def button_click():
    pass


# UI
root = tk.Tk()
root.title("Roman Numarals to Integer")

# Roma Rakamı Giriş
roman_label = tk.Label(root, text="Enter Roman Numaral")
roman_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

roman_entry = tk.Entry()
roman_entry.grid(row=1, column=0, columnspan=2, pady=15)

# Çevirme Butonu
send_button = tk.Button(root, text="Convert", command=button_click)
send_button.grid(row=2, column=0, columnspan=2, pady=10)

# Sonuç
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
