import tkinter as tk

 
# create the function for changing the color
def change_window_color():
    color_choice = color_entry.get()
    color_choice = color_choice.lower()

    if "#" in color_choice:
        if len(color_choice) < 7 or len(color_choice) > 7:
            results["text"] = "Please enter a valid hex code."
        elif color_choice == "#000000":
            window.configure(bg=color_choice)
            dir_label["bg"] = color_choice
            dir_label["fg"] = "white"
            results["text"] = ""
            results["bg"] = color_choice
        else:
            try:
                window.configure(bg=color_choice)
                dir_label["bg"] = color_choice
                results["text"] = ""
                results["bg"] = color_choice
            except:
                results["text"] = "Please enter a valid hex code"
                results["fg"] = "white"
    else:
        if color_choice == "black":
            window.configure(bg=color_choice)
            dir_label["bg"] = color_choice
            dir_label["fg"] = "white"
            results["text"] = ""
            results["bg"] = color_choice
        else:
            try:
                window.configure(bg=color_choice)
                dir_label["bg"] = color_choice
                results["text"] = ""
                results["bg"] = color_choice
            except:
                results["text"] = "please enter a valid color."
                results["fg"] = "white"
 

# create the window
window = tk.Tk()
window.title("Window Color App")
window.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

 

# create the directions
dir_label = tk.Label(text="Enter a basic color or hex code below")
dir_label.grid(row=0, column=1)

 
# create the color entry
color_entry = tk.Entry(width=10)
color_entry.grid(row=1, column=1)

 
# create the button that calls the change_window_color function with the call
change_button = tk.Button(relief=tk.RAISED, borderwidth=3, text="Click to Change Colors", command=change_window_color)
change_button.grid(row=2, column=1)
 

# Create the results area
results = tk.Label(text="")
results.grid(row=3, column=1)

# keep the app running
window.mainloop()