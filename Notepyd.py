#-------------------------------------------------------
"""
This script is made by Tijndagamer and released under the MIT license.
"""
#-------------------------------------------------------

#Imports and varia
import pickle

#-------------------------------------------------------

#Functions tab
def help():
    print("These are the available commands:")
    print("make new doc")
    print("view doc")
    print("help")
    print("bye")
def make_new_doc():
    filename = raw_input("name =")
    filename = filename + ".pydoc"
    print("----- Editing " + filename + " -----")
    additions = raw_input("")
    print("Saving file.")
    pickle.dump(additions, open(filename, "wb"))
    print("File saved.")
def view_doc():
    filename = raw_input("name =")
    filename = filename + ".pydoc"
    view = pickle.load(open(filename, "rb"))
    print(view)

#-------------------------------------------------------

#while loop
def while_loop():
    while True:
        cmd = raw_input(">")
        if cmd == "view doc":
            view_doc()
        if cmd == "make new doc":
            make_new_doc()
        if cmd == "help":
            help()
while_loop()
