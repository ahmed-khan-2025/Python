import tkinter as tk
from tkinter import messagebox
def onSubmit():
    name = entry.get()
    SelectedGender = genderVar.get()
    subcribed = subscribeVar.get()
    SelectedLanguage = languageVar.get() 
    info = f"Name: {name}, Gender: {SelectedGender}, Subcribed: {subcribed}, language: {SelectedLanguage}"
    messagebox.showinfo("Submitted Info", info)

# Create main window
root = tk.Tk()
root.title("Interactive UI Demo")
root.geometry("350x350")

# Entry widget
label_name = tk.Label(root, text ="Name:")
label_name.pack(pady=(10,1))
entry = tk.Entry(root)
entry.pack(pady=(10,0))

# Radio buttons for gender
label_gender = tk.Label(root, text="Gender:")
label_gender.pack(pady=(10,0))

genderVar = tk.StringVar(value="Other")
radio_male = tk.Radiobutton(root, text="Male", variable= genderVar, value="Male")
radio_male.pack()

radio_female = tk.Radiobutton(root, text="Female",variable=genderVar, value="Female")
radio_female.pack()

radio_other = tk.Radiobutton(root, text="Other", variable= genderVar, value="Other")
radio_other.pack()
# Checkbox for subscription
subscribeVar = tk.BooleanVar()
check_box = tk.Checkbutton(root, text="Subscribe to newsletter", variable= subscribeVar)
check_box.pack()
# Dropdown menu for favorite language
label_language = tk.Label(root, text="Favorite Language:")
label_language.pack(pady=(10,0))

languages = ["Python", "JavaScript", "Java", "C++", "C#"]
languageVar = tk.StringVar(value=languages[0])

dropDown = tk.OptionMenu(root, languageVar, *languages)
dropDown.pack(pady=(5,0))
# Submit button
submitButton = tk.Button(root, text="Submit" , command=onSubmit)
submitButton.pack(pady=(10,0))
# Start the GUI loop
root.mainloop()