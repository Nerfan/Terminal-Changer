"""
Read colors from a current xfce4-terminal configuration and save to .Xresources
"""

def extract_colors(filename):
    """
    Get the line containing color codes

    Args:
        filename (str): Path to terminalrc file

    Returns:
        str: All color codes in order
    """
    file = open(filename)
    for line in file:
        if line[0:12] == "ColorPalette":
            return line[13:-2]
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
    print(colors)
    for color in colors: # TODO vary based on 6 or 12 digit
        newcolor = "#" + color[1:3] + color[5:7] + color[9:11]
        newcolors.append(newcolor)
    return newcolors

def apply_colors(colors):
    """
    Apply colors to .Xresouces
    
    Args:
        colors (list of str): Colors to apply, in order
    """
    i = 0
    xresources = open("/home/jeremy/.Xresources")
    text = ""
    for line in xresources:
        if (line[1:7] == "color" + str(i)):
            text += line[0:9] + "       " + colors[i] + "\n"
            i += 1
        elif (line[1:8] == "color" + str(i)):
            text += line[0:9] + "       " + colors[i] + "\n"
            i += 1
        else:
            text += line
    xresources.close()
    xresources = open("/home/jeremy/.Xresources", "w")
    xresources.truncate()
    xresources.write(text)
    xresources.close()

apply_colors(change_color_codes(extract_colors("/home/jeremy/.config/xfce4/terminal/terminalrc")))
