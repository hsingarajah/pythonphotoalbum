import os

def printDir(dir):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Current working directory, {dir}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myDir = os.getcwd()
    printDir(myDir)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
