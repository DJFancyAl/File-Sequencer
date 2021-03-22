# File-Sequencer
Will iterate through the files in a folder and rename them with a number sequence.

### What it does:
* Asks for the file directory containing the files to be changed.
* Asks for a "prefix", which will be at the start of the new file names.
* Will then rename all the files in  the directory with a new file name that has the same file extension.

### Example:
If the directory contains image files such as:
* dsc_092821.png
* dsc_100721.png
* dsc_100821.png 
  
Then user must input the directory containing these files and a prefix (maybe "photo"). The script will then rename
the files to:
* photo001.jpg
* photo002.jpg
* photo003.jpg
