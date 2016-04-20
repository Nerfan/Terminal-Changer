# Terminal-Changer
Swaps color configurations for xfce4-terminal

The colorsToXfce4Terminal.py script fetches colors (in order) from a file that contains 6-digit color codes. I use this when I find a terminal color configuration I like so that I don't have to manually change the 6-digit codes to 12-digit ones (xfce4-terminal only takes 12-digit color codes in the terminalrc config file).

The changeColorScheme.py script does exactly what it sounds like. It takes a file containing a colorscheme and (optionally) a foreground and background color and applies it to terminalrc. The default in the file is set to my terminalrc path, but it should be easy to change that. You call the script with:
python3 changeColorScheme.py [save|load] configFile [fg] [bg]
If save or load is not specified, the script assumes load.
