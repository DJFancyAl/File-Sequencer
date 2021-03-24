import os
import re


def rename_files(name, extension):
    sequence = 1
    # List Current Files in Directory
    for file in os.listdir():
        os.rename(file, "{}{:03d}{}".format(name, sequence, extension[0]))
        sequence += 1
    print("Files have been renamed!")
    return False


def check_files(location):
    # Change the working directory based off the file_directory input
    os.chdir(location)

    file_list = []
    for file in os.listdir():
        # Adds all file extensions to a list.
        file_list.append(file)

    extension1 = re.findall(r"(\.\w+)$", file_list[0])
    for file in file_list:
        extension2 = re.findall(r"(\.\w+)$", file)
        # Checks if the file extensions are all the same.
        if extension1 != extension2:
            print("Files in the directory are not all the same file type. Please try another directory.\n"
                  "*******************************************\n")
            return True

    return rename_files(prefix, extension1)


run = True
while run:
    # Set the variables to create filename
    file_directory = input("Directory where files are located?\n")
    prefix = input("Prefix for the file name (same with each filename)?\n")
    run = check_files(file_directory)
