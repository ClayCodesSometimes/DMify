import tkinter as tk

window = tk.Tk()
window.title("DMify")
window.geometry("1920x1080")

label = tk.Label(window, text="Welcome to DMify!", font=("Helvetica", 24))
label.pack(pady=20)

button = tk.Button(window, text="Stop", width=25, command=window.destroy)
button.pack()

label = tk.Label(window, text="What game are you playing?", font=("Helvetica", 12))
label.pack(pady=20)

lb = tk.Listbox(window)
lb.insert(1, "D&D")
lb.insert(2, "Daggerheart")
lb.insert(3, "Pathfinder")
lb.insert(4, "Other")
lb.pack()

menu = tk.Menu(window)
window.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")


window.mainloop()