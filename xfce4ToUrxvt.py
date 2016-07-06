def extractColors(filename):
    file = open(filename)
    for line in file:
        if line[0:12] == "ColorPalette":
            return line[13:-2]
    return ""

def changeColorCodes(colorLine):
    colors = colorLine.split(";")
    newcolors = []
    print(colors)
    for color in colors:
        newcolor = "#" + color[1:3] + color[5:7] + color[9:11]
        newcolors.append(newcolor)
    return newcolors

def applyColors(colors):
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

applyColors(changeColorCodes(extractColors("/home/jeremy/.config/xfce4/terminal/terminalrc")))
