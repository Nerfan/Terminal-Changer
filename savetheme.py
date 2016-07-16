"""
Save the current color scheme to a preset
"""

import sys
from os import getenv, makedirs
from os.path import isdir
HOME = getenv("HOME")

def get_colors():
    """
    Get all of the color options from the current terminalrc

    Returns:
        str: All color options as they appeared in the terminalrc file
    """
    terminalrc = open(HOME + "/.config/xfce4/terminal/terminalrc")
    colors = ""
    for line in terminalrc:
        if line[0 : 5] == "Color":
            colors += line
    terminalrc.close()
    return colors

def write_scheme(theme_name, color_options):
    """
    Save options to a preset

    Args:
        theme_name (str): Name of the theme to be saved
        color_options (str): Any and all options to be saved
                            These just get written directly to a file
    """
    if not isdir(HOME + "/.local/share/xfce4/terminal/colorschemes"):
        makedirs(HOME + "/.local/share/xfce4/terminal/colorschemes")
    scheme_file = open((
        HOME + "/.local/share/xfce4/terminal/colorschemes/" +\
        theme_name + ".theme"), "w+")
    scheme_file.write(
        "[Scheme]\n"
        + "Name=" + theme_name + "\n"
        + color_options)
    scheme_file.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("usage: python3.5 savetheme.py themename")
    else:
        write_scheme(sys.argv[1], get_colors())
