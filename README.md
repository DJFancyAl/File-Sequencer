# File-Sequencer

## Purpose

The __"File Sequencer"__ was created for a specific situation - when you have A LOT of files which are poorly named and as such are tough to keep organized. For example - you may have downloaded a folder containing photos from your trip to Cancun. The image files have exotic file names such as `dsc_092821.png`, `dsc_100721.png`, and `dsc_100821.png`.

These file names are frustrating! They don't provide any information about what's in the photo and they are not in an easily readable order. This is where the __File Sequencer__ can help - we can quickly change hundred or even thousands of filenames like the ones above into more readable names like `Cancun001.png`, `Cancun002.png`, and `Cancun003.png`


| Old File       |      | New File      |
| -------------- | ---- | ------------- |
| dsc_092821.png | ---> | Cancun001.png |
| dsc_100721.png | ---> | Cancun002.png |
| dsc_100821.png | ---> | Cancun003.png |

__See!__ Isn't that much better? The file sequence works with files of any type, and is not only limited to image files. It works equally well with .doc, .pdf, .mp3, or any other file type you may have.

## Setup

In order for the __File Sequencer__ to work a few things need to be true:
1. All of the files you will be renaming need to be in the same directory. A good practice would be to create a new directory and drag all of your files into it.
2. All of the files in the directory must have the same file extension. If only 1 file has a different extension then the script will not run.
3. You must be sure that you want the file names to be changed. This script does not create a copy of the files but __WILL RENAME__ each and every one of them. This function is not easily undone.

## Sequencing Files

Once you have completed the setup above, you are ready to begin sequencing those files! Open the command line and change directory to the location of the __File Sequencer__. Use Python to run the script. The command should look something like:

`python3 sequence_files.py` or `py sequence_files.py`

The script will now ask a short series of questions, starting with _Directory where files are located?_ Enter or paste the absolute directory where your files are location it should be something like this: `C:\Users\You\Documents\vacation_photos\` Once you've entered this value press enter to continue.

The next question is _Prefix for the file name (same with each filename)?_ This will be what will be added to the start of your new file names. This value may be a data, location, or some other description. Once you've added your prefix, hit "enter".

The __file sequencer__ will now show you a preview of the file changes that will occur. Take a close look at them to make sure that the end result is what you're looking for.

The script will then ask _Would you like to continue with file change?_ THIS IS YOUR LAST CHANCE! If you don't want to change the files then close the command line. If you are ready to change your files, then type "y" or "yes".

Your files will quickly be renamed and you will see a completion message. You can now navigate to the directory containing your files. You should see that the files have flashy new names!

## File History

You may also notice that there is one new file in this directory. That is the _file_history.csv_ file. This is a file created by the script JUST IN CASE you needed to look back at the previous file names. In future updates this file will be used to revert to the previous file names. However, for now it can only be used for reference. If you are certain that you will not never need the previous file names, then you may delete this file.
