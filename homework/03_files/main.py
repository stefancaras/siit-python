import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import csv


def load_data(column, my_filter, sort):
    global prev_col
    global a_bool
    a_bool = not a_bool if column == prev_col else False
    with open('tasks.csv') as tasks:
        my_tasks = list(csv.reader(tasks))
        sorted_list = sorted(my_tasks[1:], key=lambda e: e[column].lower(), reverse=a_bool) if sort else my_tasks[1:]
        filtered = filter(lambda e: my_filter.lower() in ','.join(e).lower(), sorted_list) if my_filter else sorted_list
        treeview.delete(*treeview.get_children())
        for col in my_tasks[0]:
            treeview.heading(col, text=col, command=lambda c=col: load_data(my_tasks[0].index(c), my_filter, True))

        for value in filtered:
            treeview.insert('', tk.END, values=value)
    prev_col = column


def insert_row():
    with open('tasks.csv', mode='r+') as tasks:
        row_values = [task.get(), date.get(), responsible.get(), category.get()]
        csv_reader = list(csv.reader(tasks))
        categories = [items[3] for items in csv_reader][1:]
        task_list = [items[0] for items in csv_reader]

        if category.get() not in categories:
            if not messagebox.askyesno("askyesno", "The category does not exist, add category?"):
                return
        if task.get() in task_list:
            messagebox.showerror("showerror", "Task exists.")
            return

        treeview.insert('', tk.END, values=row_values)
        csv.writer(tasks).writerow(row_values)

        # Clear fields
        task.delete(0, "end")
        task.insert(0, "Task")
        responsible.delete(0, "end")
        responsible.insert(0, "Person responsible")
        category.delete(0, "end")
        category.insert(0, "Category")


def delete_row():
    if messagebox.askyesno("askyesno", "Do you want to delete task?") and treeview.focus():
        element = treeview.item(treeview.focus())['values'][0]
        with open('tasks.csv', mode='r') as tasks:
            csv_reader = list(csv.reader(tasks))
            csv_reader = list(filter(lambda x: x[0] != element, csv_reader))
        with open('tasks.csv', mode='w') as tasks:
            csv.writer(tasks).writerows(csv_reader)
        load_data(3, a_filter.get(), False)


prev_col = None
a_bool = False

root = tk.Tk()
root.tk.call("source", "forest-dark.tcl")
ttk.Style(root).theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()

filter_frame = ttk.LabelFrame(frame, text="Filter")
filter_frame.grid(row=0, column=0, padx=20, pady=10)

a_filter = ttk.Entry(filter_frame)
a_filter.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")
a_filter.bind("<KeyRelease>", lambda e: load_data(3, a_filter.get(), False))

widgets_frame = ttk.LabelFrame(frame, text="Insert Row")
widgets_frame.grid(row=1, column=0, padx=20, pady=10)

task = ttk.Entry(widgets_frame)
task.insert(0, "Task")
task.bind("<FocusIn>", lambda e: task.delete('0', 'end'))
task.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")

date = DateEntry(widgets_frame, showweeknumbers=False)
date.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="ew")

responsible = ttk.Entry(widgets_frame)
responsible.insert(0, "Person responsible")
responsible.bind("<FocusIn>", lambda e: responsible.delete('0', 'end'))
responsible.grid(row=2, column=0, padx=5, pady=(0, 5), sticky="ew")

category = ttk.Entry(widgets_frame)
category.insert(0, "Category")
category.bind("<FocusIn>", lambda e: category.delete('0', 'end'))
category.grid(row=3, column=0, padx=5, pady=(0, 5), sticky="ew")

button = ttk.Button(widgets_frame, text="Insert", command=insert_row)
button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

tree_frame = ttk.Frame(frame)
tree_frame.grid(row=0, column=1, rowspan=2, pady=10)
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")

cols = ("Task", "End date", "Person responsible", "Category")
treeview = ttk.Treeview(tree_frame, show="headings", yscrollcommand=tree_scroll.set, columns=cols, height=13)
treeview.column("Task", width=100, anchor='center')
treeview.column("End date", width=100, anchor='center')
treeview.column("Person responsible", width=150, anchor='center')
treeview.column("Category", width=100, anchor='center')
treeview.pack()
tree_scroll.config(command=treeview.yview)
load_data(3, "", True)

treeview.bind("<KeyPress>", lambda e: delete_row() if e.keysym == 'Delete' else 0)

root.mainloop()
