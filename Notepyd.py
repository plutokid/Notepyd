#-------------------------------------------------------
"""
This script is made by Tijndagamer and released under the MIT license.
"""
#-------------------------------------------------------

#Imports and varia
import pickle

#-------------------------------------------------------

def make_new_doc():
    filename = raw_input("name =")
    filename = filename + ".pydoc"
    print("----- Editing " + filename + " -----")
    additions = raw_input("")
    print("Saving file.")
    pickle.dump(additions, open(filename, "wb"))

#-------------------------------------------------------
