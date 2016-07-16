# Terminal-Changer
Small scripts that I made to make my terminal configuring life easier.

Since nobody uses xfce4-terminal and everyone uses urxvt, I wanted to make something to change a .Xresources terminal color scheme into one compatible with xfce4-terminal.
Thus the xresourcestoxfce4.py script was created. Simply running it with no arguments takes the colors in ~/.Xresources and applies them in ~/.config/xfce4/terminal/terminalrc.
You can also supply arguments ti direct the script to read from and write to specific locations. The arguments come in that order. For example:
```
$ python3.5 xresourcestoxfce4.py colorsource.txt terminalrclocation
```

xfce4toxresources.py does the exact opposite; it takes the current color scheme of xfce4-terminal and applies it in .Xresources.
At the moment no command line arguments are supported. This will probably change soon.

savetheme.py does exactly what the name would imply: it saves the current xfce4-terminal colorscheme as a preset scheme.
Enter the name of the theme as a command line argument; i.e.
```
$ python3.5 savetheme.py themename
```
