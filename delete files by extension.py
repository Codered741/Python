import os
import glob
import shutil

delDir = "_DeleteMe\\"

searchDir = input("Enter the directory you want to search. >>"
if type(searchDir) is not str:
    print("Please enter a string, in the format 'C:\DirectoryName\'")
    exit
    
searchExt = input("Enter the file extension you want to remove. e.g. .ipj >>")
if type(searchExt) is not str:
    print("Please enter a string, in the format '.exe'")
    exit

for fname in glob.glob(searchDir + "**\\**" + searchExt, recursive=True):  #
    print (fname)
    if not os.path.exists(searchDir + delDir):
        os.makedirs(searchDir + delDir)
        
    shutil.copy(fname, searchDir + delDir)
    os.remove(fname)
    
print ("The files listed above were removed")
