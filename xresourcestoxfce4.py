"""
Take an .Xresources file and apply the colorscheme to xfce4-terminal

The file doesn't have to be the .Xresources file, just in the same format.
Enter the filename as a command line argument if not .Xresources.
The script then scans for colors in the file and applies them to the terminal.
Designed because I wanted a reusable script to change
.Xresources config files into ones usable with xfce4-terminal.
"""

import sys
from os import getenv

HOME = getenv("HOME")

def get_new_colors(filename):
    """
    Take a file and "extract" all of the color codes from it.

    Args:
        filename (str): Path to file containing color codes

    Returns:
        str: any color codes found in the text separated by semicolons
    """
    color_list = [""]*16
    for line in open(filename):
        for i in range(len(line)):
            if line[i:i+5] == "color" and line[i+5].isdigit():
                index = line[i+5]
                if line[i+6] != ":":
                    index = line[i+5:i+7]
                index = int(index)
                color_list[index] = line.split()[1]
    new_colors = ""
    for color in color_list:
        new_colors += color + ";"
    return new_colors[:-1]

def set_colors(new_colors, terminalrc_location):
    """
    Take a string of color codes and apply to terminalrc.

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

def main(sourcefile=HOME + "/.Xresources", terminalrc=HOME + "/.config/xfce4/terminal/terminalrc"):
    """
    Loop through a file and change the current settings in terminalrc

    Args:
        sourcefile (str): Name of file to open containing the source colors
        terminalrc (str): Path to terminalrc file
    """
    new_colors = get_new_colors(sourcefile)
    set_colors(new_colors, terminalrc)

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("Usage: python3.5 colorsToXfce4Terminal.py [sourcefile] [terminalrc]")
        exit(0)
    elif len(sys.argv) < 2:
        main()
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main(sys.argv[1], sys.argv[2])
