import os
import re


def create_history(name, extension, list):
    # Display a list of current file names
    print("New file names will look like this:")
    i = 0
    sequence = 1
    old_name_length = 0
    for i in range(5):
        # Define variables
        old_name = list[i]
        if len(old_name) > old_name_length:
            # Sets longest file length for formatting
            old_name_length = len(old_name)
        i += 1

    for i in range(5):
        old_name = list[i]
        new_name = "{}{:03d}{}".format(name, sequence, extension)
        print('{:>{}s} ----> {}'.format(old_name, old_name_length, new_name))
        i += 1
        sequence += 1

    verify = input("**********************************\nWould you like to continue?\n")

    if verify.lower() == 'y' or verify.lower() == 'yes':
        pass

    print("Okay. Let's try again.\n")
    return True


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

    return create_history(prefix, extension1[0], file_list)


run = True
while run:
    # Set the variables to create filename
    file_directory = input("Directory where files are located?\n")
    prefix = input("Prefix for the file name (same with each filename)?\n")
    run = check_files(file_directory)
