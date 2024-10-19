"""
Log Search using a Id-Name Dictionary
"""
import tkinter as tk
from tkinter import simpledialog, messagebox
# TODO: Create a dictionary of integers for the keys and strings for the values.
#  Create a GUI app with three buttons. Look at 'log_search_example.png' in this
#  folder for an example of what your program should look like.
#
#  Button 1: Add Entry
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      After an ID is entered, use another input dialog to ask the user
#      to enter a name. Add this information as a new entry to your
#      dictionary.
Root = tk
dic = {}
def Add_Entry_func():
    print("works!")
    key = simpledialog.askinteger(title= "ID", prompt= "Please enter a integer." )
    value = simpledialog.askstring(title = "NAME", prompt= "Please enter a name.")
    if "jay" in value or "Jay" in value:
        key = 69
        value = "u tried buddy imma destroy u next week"
        messagebox.showinfo(title= "sussy error", message= f"""oops ur keys and values got hacked by someone and now it's this:
        {key} and {value} if this error occured to you then womp womp""")
    dic.update({key : value})
Add_Entry = tk.Button(text = "Add", command = Add_Entry_func)
Add_Entry.place(relx = 0.1, rely = 0.1, relheight = 0.1, relwidth = 0.1)
#  Button 2: Search by ID
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      If that ID exists, display that name to the user.
#      Otherwise, tell the user that that entry does not exist.
#
def Search_By_ID():
    key = simpledialog.askinteger(title="ID", prompt="Please enter an ID.")
    if key not in dic:
        messagebox.showerror(title= "ERROR", message= "sorry that ID doesn't exist.")
    else:
        val = dic[key]
        messagebox.showinfo(title= "", message= f"the value you are looking for is, {val}")

Search_Button = tk.Button(text = "Search", command = Search_By_ID)
Search_Button.place(relx = 0.25, rely = 0.1, relheight = 0.1, relwidth = 0.15)
# Button 3: View List
#      When this button is clicked, display the entire list in a message
#      dialog in the following format:
#      ID: 123  Name: Harry Howard
#      ID: 245  Name: Polly Powers
#      ID: 433  Name: Oliver Ortega
#      etc...
#
def View_dictionary():
    revised_dic = ""
    count = 0
    for key in dic:
        if dic[key] == "u tried buddy imma destroy u next week":

            revised_dic += f"ID: {key} Name: {dic[key]} <-- oop there's a error in here too womp womp"
            revised_dic += """
        """
        else:
            revised_dic += f"ID: {key} Name: {dic[key]} "
            revised_dic += """
                    """
    messagebox.showinfo(title= "dictionary", message= revised_dic)
View_Button = tk.Button(text= "View", command = View_dictionary)
View_Button.place(relx = 0.45, rely = 0.1, relheight = 0.1, relwidth = 0.1)
# When this is complete, add a fourth button to your window.
# Button 4: Remove Entry
#      When this button is clicked, prompt the user to enter an ID using
#      an input dialog.
#      If this ID exists in the dictionary, remove it. Otherwise, notify the
#      user that the ID is not in the list.
def Remove_Key():
     Removing_ID = simpledialog.askinteger(title= "Removing Key...", prompt= "What ID do you wish to remove?")
     if Removing_ID in dic:
         del dic[Removing_ID]
     else:
        messagebox.showerror(title= "EEP EEP", message= "NO KEY IN DICTIONARY WOMP WOMP")
Removing_Button = tk.Button(text = "Remove", command = Remove_Key)
Removing_Button.place(relx = 0.6, rely =0.1, relheight = 0.1, relwidth = 0.13)
Root.mainloop()