import tkinter as tk

# Window
root = tk.Tk()
root.geometry("400x400")
root.title("TkInter App")

# Label
label = tk.Label(master=root, text="TkInter App", bg="lightblue", fg="black")
label.pack(pady=20)

# Entry
entry = tk.Label(master=root, width=30, bg="lightblue", fg="navy")
entry.pack(pady=30)

# Button
button = tk.Button(master=root, text="Click here")
button.pack(pady=20)

root.mainloop()
