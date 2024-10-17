import tkinter
import tkinter.messagebox
import pickle

#To Create the root window
root = tkinter.Tk()
root.title("To-Do List")

# Function to add a task
def add_task():
    task = entry_task.get()  # Get the task from the input field
    if task != "":  # Check if the input is not empty
        listbox_tasks.insert(tkinter.END, task)  # Insert the task at the end of the listbox
        entry_task.delete(0, tkinter.END)  # Clear the input field after adding
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]  # Get the index of the selected task
        listbox_tasks.delete(task_index)  # Delete the selected task
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

# Function to load tasks from a file
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))  # Load the tasks from the file
        listbox_tasks.delete(0, tkinter.END)  # Clear the current tasks in the listbox
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)  # Insert the loaded tasks into the listbox
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

# Function to save tasks to a file
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())  # Get all tasks from the listbox
    pickle.dump(tasks, open("tasks.dat", "wb"))  # Save the tasks to the file

# Create the GUI components
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

# Listbox for displaying tasks
listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

# Scrollbar for the listbox
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Entry field for new tasks
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

# Buttons for add, delete, load, and save operations
button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()

# Start the main loop
root.mainloop()

