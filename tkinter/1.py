# step 1: Import the tkinter
import tkinter as tk

# Step 2: Create the root window 
root= tk.Tk()
root.title("My First GUI App")

root.geometry("400x300")

# Step 3: Create a label widget
label = tk.Label(root, text="Hello, World!", font=("Arial",24))
label.pack(pady=20)

# Step 4 : Create a button Widget
def on_button_click():
    label.config(text="Button clicked!")

button = tk.Button(root,text="Click Me",command=on_button_click)
button.pack(pady=10)

root.mainloop()