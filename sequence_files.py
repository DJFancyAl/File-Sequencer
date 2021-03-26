import os
import re
import csv


def check_files(location, name):
    # Change the working directory based off the file_directory input
    if not os.path.isdir(location):
        print("That directory does not exist...try again.\n")
        return True
    os.chdir(location)

    file_list = []
    new_list = []
    sequence = 1

    for file in os.listdir():
        # Adds all file extensions to a list.
        if file != 'file_history.csv':
            file_list.append(file)

    extension1 = re.findall(r"(\.\w+)$", file_list[0])
    for file in file_list:
        # Create a new_file_list for use in later functions.
        new_list.append("{}{:03d}{}".format(name, sequence, extension1[0]))
        sequence += 1
        # Checks if the file extensions are all the same.
        extension2 = re.findall(r"(\.\w+)$", file)
        if extension1 != extension2:
            print("Files in the directory are not all the same file type. Please try another directory.\n"
                  "*******************************************\n")
            return True

    return show_demo(file_list, new_list)


def show_demo(name_list, new_name_list):
    # Display a list of current file names
    print("New file names will look like this:")
    sequence = 1
    old_name_length = 0
    for i in range(5):
        # Define variables
        old_name = name_list[i]
        if len(old_name) > old_name_length:
            # Sets longest file length for formatting
            old_name_length = len(old_name)
        i += 1

    for i in range(5):
        old_name = name_list[i]
        new_name = new_name_list[i]
        print('{:>{}s} ----> {}'.format(old_name, old_name_length, new_name))
        i += 1
        sequence += 1

    verify = input("**********************************\nWould you like to continue with file change?\n")

    if verify.lower() == 'y' or verify.lower() == 'yes':
        return create_history(name_list, new_name_list)

    print("Okay. Let's try again.\n")
    return True


def create_history(old_list, new_list):
    history_list = dict(zip(old_list, new_list))
    with open('file_history.csv', 'w', newline="") as file_csv:
        writer = csv.writer(file_csv)
        for file in history_list:
            writer.writerow([file] + [history_list[file]])

    rename_files(new_list)


def rename_files(new_names):
    sequence = 0
    # List Current Files in Directory
    for file in os.listdir():
        if file != 'file_history.csv':
            os.rename(file, new_names[sequence])
            sequence += 1
    print("Files have been renamed!")
    return False


run = True
while run:
    # Set the variables to create filename
    file_directory = input("Directory where files are located?\n")
    prefix = input("Prefix for the file name (same with each filename)?\n")
    run = check_files(file_directory, prefix)
