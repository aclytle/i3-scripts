Sharing my i3 scripts and config as is. Many things won't work, like my
hosts file switcher keybinds and my lockscript. You can make your own or
comment out those lines. If you really want to see my other configs, or scripts,
file an issue

Features:
workspacer.py script allows easy use of 10+ workspace
renamer.py uses dmenu to rename workspaces on the fly
clipboard management with xcmenu
extra top i3bar to handle the extra workspaces
Various extra keybindings and tweaks
Red/green retina burning window borders

i3-wm scripts provided require i3ipc. To install:
sudo pip install i3ipc

The workspace renamer script is really handy. It's bound to alt-y in my config

The workspacer.py script lets you easily switch between 10+ workspaces.
Look at my config for an example on how to use it. If you use my config:
Use alt-up and alt-down to jump up and down by 10. shift-alt-up and 
shift-alt-down will move windows up and down by 10. I often use the mouse
and i3bar to jump to named workspaces that are more than 2 keybinds away.
I use this currently on a single monitor setup, you'll want to reconfigure
a bit for a multi-monitor setup.

Recommend you install xcmenu:
https://github.com/Cloudef/xcmenu
alt-u to browse clipboard history

Make sure you put all this in your $HOME/.i3/ directory
