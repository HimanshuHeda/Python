# WAP to create a window 80*56 bg color green text size 56 font times new roman 

import tkinter as tk

# Create the root window 
root = tk.Tk()


# Configure the root window
root.title("Advance Root Window")
root.geometry("800x560")        # Set width and height
root.configure(bg="green")      # Change background color 

# Add a label to the root window 
label = tk.Label(root, text="Welcome !!", font=("times new roman",56), bg="red")
label.pack(pady=20)


# Add an exit button 
def close_app():
    root.quit()

exit_button=tk.Button(root,text="Exit",command=close_app)
exit_button.pack(pady=10)

# Start the main event loop
root.mainloop()