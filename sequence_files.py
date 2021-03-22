import os
import re


def rename_files(location, prefix):
    # Change the working directory based off the file_directory input
    os.chdir(location)
    sequence = 1
    # List Current Files in Directory
    for file in os.listdir():
        extension = re.findall(r"(\.\w+)$", file)
        os.rename(file, "{}{:03d}{}".format(prefix, sequence, extension[0]))
        sequence += 1


# Set the variables to create filename
file_directory = input("Directory where files are located?\n")
prefix = input("Prefix for the file name (same with each filename)?\n")

rename_files(file_directory, prefix)
print("Files have been renamed!")
