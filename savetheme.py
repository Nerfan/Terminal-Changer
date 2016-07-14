"""
Save the current color scheme to a preset
"""

import sys

def get_colors():
    """
    Get all of the color options from the current terminalrc

    Returns:
        str: All color options as they appeared in the terminalrc file
    """
    terminalrc = open("/home/jeremy/.config/xfce4/terminal/terminalrc")
    colors = ""
    for line in terminalrc:
        if line[0 : 5] == "Color":
            colors += line
    terminalrc.close()
    return colors

def write_scheme(name, color_options):
    """
    Save options to a preset

    Args:
        name (str): Name of the theme to be saved
        color_options (str): Any and all options to be saved
                            These just get written directly to a file
    """
    schemeFile = open((
        "/usr/share/xfce4/terminal/colorschemes/" + name + ".theme"), "w")
    schemeFile.write(
            "[Scheme]\n"
            + "Name=" + name + "\n"
            + color_options)
    schemeFile.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        name = input("Name of theme to be saved? ")
    else:
        name = sys.argv[1]
    try:
        write_scheme(name, get_colors())
    except PermissionError:
        print("Could not access necessary directory. Try running with sudo?")
