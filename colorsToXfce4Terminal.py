"""
Take an input file containing 6-digit color codes and sets them as my xfce4-terminal colorsceheme.

Enter the filename as a command line argument.
The script then prints to the terminal all color codes found in the file.
It returns the 12-digit color codes separated by commas, which are then piped into the terminalrc file.
Designed because I wanted a reusable script to change typical config files into ones usable with xfce4-terminal.
"""

import sys

def changeColor(colorCode):
    """
    Take a 6-digit color code and return a 12-digit equivalent.

    The color code must be prefixed by the accompanying "#" symbol.

    colorCode: String, color code in the form of #123456
    return: String, color code in the form #112233445566
    """
    newColorCode = "#"
    newColorCode += colorCode[1:3] + colorCode[1:3]
    newColorCode += colorCode[3:5] + colorCode[3:5]
    newColorCode += colorCode[5:] + colorCode[5:]
    return newColorCode

def getNewColors(filename):
    """
    Take a line of text and "extract" all of the color codes from it.

    line: String, line of text with or without color codes
    return: String, any color codes found in the text, changed from 6 to 12 digit, separated by semicolons
    """
    newColors = ""
    for line in open(filename):     # For each line in the file,
        for i in range(len(line)):  # we check the letters to see 
            if line[i] == "#":      # if there is a # (indicating a color code)
                newColors += changeColor(line[i:i+7]) + ";"
    newColors = newColors[:-1] # Remove the last semicolon
    return newColors

def setColors(newColors, terminalrcLocation="/home/jeremy/.config/xfce4/terminal/terminalrc"):
    """
    Takes a string of color codes and replaces the colors currently set in terminalrc.

    Can also take an argument for where the terminalrc is
    """
    verify = input("Have you saved the current color scheme? (y/n) ")
    if verify != "y":
        print("Go ahead and do that.")
        exit(0)
    terminalrc = open(terminalrcLocation)
    filebefore = ""
    for line in terminalrc:
        if line[0:13] == "ColorPalette=":
            filebefore += line[0:13] + newColors + "\n"
        else:
            filebefore += line
    terminalrc.close()
    terminalrc = open(terminalrcLocation, "w")
    terminalrc.truncate()
    terminalrc.write(filebefore)
    terminalrc.close()

def main(args):
    """
    Loop through a file and change the current settings in terminalrc

    filename: String, name of file to open containig 6-digit color codes to change
    """
    newColors = getNewColors(args[1])
    if (len(args) == 3):
        setColors(newColors, args[2])
    else:
        setColors(newColors)

if __name__=="__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3: # Need a filename (this file counts as the first argument)
        print("Usage: python3.5 colorsToXfce4Terminal.py filename [location of terminalrc]")
        exit(0)
    main(sys.argv)
