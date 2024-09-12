# WAP to create a window with 2 buttons of any size any color and any style and any font.

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
exit_button1=tk.Button(root,text="GetLost",command=close_app)
exit_button.pack(pady=10)
exit_button1.pack(pady=40)

# Start the main event loop
root.mainloop()