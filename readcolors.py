"""
Take an input file containing 6-digit color codes and sets them as my xfce4-terminal colorsceheme.

Enter the filename as a command line argument.
The script then prints to the terminal all color codes found in the file.
It returns the 12-digit color codes separated by commas, which are then piped into the terminalrc file.
Designed because I wanted a reusable script to change Xresources config files into ones usable with xfce4-terminal.
"""

import sys
from os import getenv

HOME = getenv("HOME")

def get_new_colors(filename):
    """
    Take a line of text and "extract" all of the color codes from it.

    Args:
        line: String, line of text with or without color codes

    Returns:
        String: any color codes found in the text separated by semicolons
    """
    colorList = [""]*16 
    for line in open(filename):     # For each line in the file,
        for i in range(len(line)):  # we check the letters to see 
            if line[i:i+5] == "color":
                index = line[i+5]
                if line[i+6] != ":":
                    index = line[i+5:i+7]
                index = int(index)
                colorList[index] = line.split()[1]
    new_colors = ""
    for color in colorList:
        new_colors += color + ";"
    return new_colors[:-1]

def set_colors(new_colors, terminalrc_location=HOME + "/.config/xfce4/terminal/terminalrc"):
    """
    Take a string of color codes and replace the colors currently set in terminalrc.

    Can also take an argument for where the terminalrc is

    Args:
        new_colors (str): 16 color codes separated by semicolons (no spaces)
        terminalrc_location (str): Path to the xfce4-terminal config file
    """
    verify = input("Have you saved the current color scheme? (y/n) ")
    if verify != "y":
        print("Go ahead and do that.")
        exit(0)
    terminalrc = open(terminalrc_location)
    filebefore = ""
    for line in terminalrc:
        if line[0:13] == "ColorPalette=":
            filebefore += line[0:13] + new_colors + "\n"
        else:
            filebefore += line
    terminalrc.close()
    terminalrc = open(terminalrc_location, "w")
    terminalrc.truncate()
    terminalrc.write(filebefore)
    terminalrc.close()

def main(args):
    """
    Loop through a file and change the current settings in terminalrc

    filename: String, name of file to open containing 6-digit color codes to change
    """
    new_colors = get_new_colors(args[1])
    if (len(args) == 3):
        set_colors(new_colors, args[2])
    else:
        set_colors(new_colors)

if __name__=="__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3: # Need a filename (this file counts as the first argument)
        print("Usage: python3.5 colorsToXfce4Terminal.py filename [location of terminalrc]")
        exit(0)
    main(sys.argv)
