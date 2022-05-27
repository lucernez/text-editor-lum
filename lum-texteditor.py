from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("LUM")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
my_frame = Frame(window)
my_frame.pack(pady=5)  
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)
my_text = Text(my_frame, width=97, height=25, font=("Helivca", 16), undo=True,selectforeground="Black", yscrollcommand=text_scroll.set)
my_text.pack()
text_scroll.config(command=my_text.yview)
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    my_text.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        my_text.insert(END, text)
    window.title(f"Text Editor Application - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = my_text.get(1.0, END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)
my_menu = Menu(window)
window.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="open file", command=open_file)
file_menu.add_command(label="save file", command=save_file)
window.mainloop()