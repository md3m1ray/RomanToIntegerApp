import tkinter as tk


def convert_integer(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman:
            num += roman[s[i:i + 2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1

    result_label.config(text=str(num))


def button_click():
    convert_integer(roman_entry.get().upper())


# UI
root = tk.Tk()
root.title("Roman Numarals to Integer")
root.minsize(width=350, height=250)
root.config(padx=50, pady=50)

# Roma Rakamı Giriş
roman_label = tk.Label(root, text="Enter Roman Numaral")
roman_label.pack()

roman_entry = tk.Entry()
roman_entry.focus()
roman_entry.pack()

space_label = tk.Label(root, text="")
space_label.pack()

# Çevirme Butonu
send_button = tk.Button(root, text="Convert", command=button_click)
send_button.pack()

space_label = tk.Label(root, text="")
space_label.pack()

# Sonuç
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
