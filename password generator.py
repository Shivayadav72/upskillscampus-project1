import string
import tkinter as tk
import random
from tkinter import messagebox
import webbrowser
def generate_password(length,uppercase,lowercase,digits,special):
    all_character=""
    if uppercase:
        all_character+= string.ascii_uppercase
    if lowercase:
        all_character+= string.ascii_lowercase
    if digits:
        all_character+= string.digits
    if special:
        all_character+= string.punctuation
    if not all_character:
        raise ValueError("You must Select atleast one character type!")
    password="".join(random.choice(all_character)for _ in range(length))
    return password

# Define Function for GUi
def on_generate():
     try:
         length = int(entry_length.get())
         digit =var_digit.get()
         lowercase=var_lowercase.get()
         special=var_special.get()
         uppercase=var_uppercase.get()

         password= generate_password(length,uppercase,lowercase,digit,special)
         entry_password.delete(0,tk.END)
         entry_password.insert(0,password)
     except ValueError as e:
         messagebox.showerror("Error",str(e))


         # Define Password Copy on Clip board
def copy_to_clipboard():
    try:
     root.clipboard_clear()
     root.clipboard_append(entry_password.get())
    except Exception as e:
        messagebox  .showerror("Error",f"could not copy to clipboard:{str(e)}")


      # Create the main application window

root=tk.Tk()
root.title("Your Password save")
root.resizable(False,False)

# setting for dark theme
bg_color = "#D2AC7D"
fg_color = "#05033A"
button_color = "white"
entry_bg_color = "yellow"
root.configure(bg=bg_color)

tk.Label(root,text="Password Length:",bg=bg_color,fg=fg_color).grid(row=2,column=0,padx=10,pady=10)
entry_length=tk.Entry(root,bg=entry_bg_color,fg=fg_color,insertbackground=fg_color)
entry_length.grid(row=2,column=1,padx=10,pady=10)
var_uppercase=tk.BooleanVar()
var_lowercase=tk.BooleanVar()
var_digit=tk.BooleanVar()
var_special=tk.BooleanVar()


def OpenSourceCode():
    webbrowser.open_new( https//github.com/Shivayadav72 )

tk.Button(root,text="GitHub Project",command="OpenSourceCode",bg=button_color,fg=fg_color).grid(row=1,column=0,columnspan=2,padx=10,pady=10)



tk.Checkbutton(root, text="Uppercase letters", variable=var_uppercase, bg=bg_color, fg=fg_color,
                   selectcolor=button_color).grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Lowercase letters", variable=var_lowercase, bg=bg_color, fg=fg_color,
                   selectcolor=button_color).grid(row=3, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Digits", variable=var_digit, bg=bg_color, fg=fg_color, selectcolor=button_color).grid(
        row=4, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Special characters", variable=var_special, bg=bg_color, fg=fg_color,
                   selectcolor=button_color).grid(row=4, column=1, padx=10, pady=5, sticky="w")
tk.Button(root,text="Genertae",command=on_generate, bg=button_color,fg=fg_color).grid(row=5,column=0,columnspan=2,padx=10,pady=10)

tk.Label(root, text="Generated password:", bg=bg_color, fg=fg_color).grid(row=6, column=0, padx=10, pady=10,
                                                                              sticky="w")
entry_password = tk.Entry(root, width=50, bg=entry_bg_color, fg=fg_color, insertbackground=fg_color)
entry_password.grid(row=7, column=0, padx=10, pady=10, sticky="e", columnspan=2)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg=button_color, fg=fg_color).grid(row=8,
                                                                                                            column=0,
                                                                                                            columnspan=2,
                                                                                                            padx=10,
                                                                                                            pady=10)

    # Starting the main application loop
root.mainloop()