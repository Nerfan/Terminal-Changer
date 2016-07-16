"""
Read colors from a current xfce4-terminal configuration and save to .Xresources
"""

from os import getenv
HOME = getenv("HOME")

def extract_colors(filename):
    """
    Get the line containing color codes

    Args:
        filename (str): Path to terminalrc file

    Returns:
        str: All color codes in order
    """
    terminalrc = open(filename)
    for line in terminalrc:
        if line[0:12] == "ColorPalette":
            return line[13:-1]
    return ""

def change_color_codes(color_line):
    """
    Take a line containing color codes and return a list of color codes

    Args:
        color_line (str): Line of text containing color codes

    Returns:
        list of str: All color codes from color_line in 6-digit form
    """
    colors = color_line.split(";")
    newcolors = []
    for color in colors:
        if len(color) == 13:
            newcolor = "#" + color[1:3] + color[5:7] + color[9:11]
            newcolors.append(newcolor)
        elif len(color) == 7:
            newcolor.append(color)
    return newcolors

def apply_colors(colors):
    """
    Apply colors to .Xresouces

    Overwrites any color settings already present

    Args:
        colors (list of str): Colors to apply, in order
    """
    i = 0
    xresources = open(HOME + "/.Xresources")
    text = ""
    for line in xresources:
        if line[1:7] == "color" + str(i):
            text += line[0:9] + "       " + colors[i] + "\n"
            i += 1
        elif line[1:8] == "color" + str(i):
            text += line[0:9] + "       " + colors[i] + "\n"
            i += 1
        else:
            text += line
    while i < 16:
        text += "color" + str(i)  + ":       " + colors[i] + "\n"
        i += 1
    xresources.close()
    xresources = open(HOME + "/.Xresources", "w")
    xresources.truncate()
    xresources.write(text)
    xresources.close()

apply_colors(change_color_codes(extract_colors(HOME + "/.config/xfce4/terminal/terminalrc")))
