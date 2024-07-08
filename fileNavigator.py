import os
# os.chdir('../')   # changes current working directory
# os.startfile(path)    # like double clicking the file
# os.system('cls')  # executes cls command in shell
# os.path.isdir(path)   # returns true if path isdir

FILE = 0
DIRECTORY = 1
# windows root = "C:\\"
DELIM = "\\"
CLEAR = "cls"

# default path
path = os.getcwd()

# updates path to be previous directory
def backOne():
    global path
    pathSplit = path.split(DELIM)
    print("path", path)
    if len(pathSplit) == 1:    # root directory
        return
    pathSplit.pop()
    update = ""
    for dir in pathSplit:
        update += dir + DELIM
    path = update[:(len(DELIM)*-1)]

# returns name of the previous directory of current path
def prevName():
    global path
    arr = path.split(DELIM)
    if len(arr) >= 2:
        returner = arr[-2]  # default, non edge case
    # edge case - root directory
    if len(arr) == 1:
        returner = arr[0]
    return returner


# main program
start = input("Enter complete path of directory to start in, or just press [ENTER] to start in the directory you called fileNavigator.py from: ")
if len(start) != 0:
    path = start

while True:
    os.system(CLEAR)
    dirs = os.listdir(path + DELIM)
    printStr = ""
    count = 1
    # save[i] = (ith entry of this directory, identifier)
    save = [["0th", -1]]
    print("Select a file (starts file) or directory (switch to that directory):")
    print("Current path: " +  path + DELIM + "\n")
    for file in dirs:
        printStr += "[" + str(count) + "] " + file
        id = FILE
        # label as file or directory
        if os.path.isdir(path + DELIM + file):
            printStr += " (DIRECTORY)\n"
            id = DIRECTORY
        else:
            printStr += " (FILE)\n"
        save.append([file, id])
        count += 1
    # go back 1 directory button
    prev = prevName()
    printStr += "[" + str(count) + "] " + "Back to " + prev + " (DIRECTORY)\n"
    save.append([prev, DIRECTORY])
    # present user with menu
    selection = int(input(printStr + "\n"))
    # make sure selection is valid
    if not (1 <= selection < len(save)):
        continue
    # back 1 directory selected
    if selection == count:
        backOne()
        continue
    # user selected a file or directory
    pathSave = path
    path += DELIM + save[selection][0]
    # file, open the file
    if save[selection][1] == FILE:
        os.startfile(path)
        path = pathSave
