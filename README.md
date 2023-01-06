# File-Sequencer

## Purpose

The __"File Sequencer"__ was created for a specific situation - when you have A LOT of files which are poorly named and as such are tough to keep organized. For example - you may have downloaded a folder containing photos from your trip to Cancun. The image files have exotic file names such as `dsc_092821.png`, `dsc_100721.png`, and `dsc_100821.png`.

These file names are frustrating! They don't provide any information about what's in the photo and they are not in an easily readable order. This is where the __File Sequencer__ can help - we can quickly change hundred or even thousands of filenames like the ones above into more readable names like `Cancun001.png`, `Cancun002.png`, and `Cancun003.png`


| Old File       |      | New File      |
| -------------- | ---- | ------------- |
| dsc_092821.png | ---> | Cancun001.png |
| dsc_100721.png | ---> | Cancun002.png |
| dsc_100821.png | ---> | Cancun003.png |

__See!__ That's much better.

## Setup

## Sequencing Files

## File History

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
