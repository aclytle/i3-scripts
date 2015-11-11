#!/usr/bin/env python2

from i3ipc import Connection
from sys import argv

MAX_WORKSPACES = 40
wdict = {}

def get_current_workspace_num(con, **kwargs):
    workspaces = con.get_workspaces()
    wnum=1
    for w in workspaces:
        if w['focused'] == True:
            wnum = w['num']
            return wnum

def get_workspace_names(con, **kwargs):
    workspaces = con.get_workspaces()
    wdict = {}
    for w in workspaces:
        wdict[w['num']] = w['name']
    return wdict

def move_window_up(con, **kwargs):
    wdict = get_workspace_names(con)
    newnum = (get_current_workspace_num(con) + 10) % MAX_WORKSPACES
    if newnum in wdict:
        newname = wdict[newnum]
    else:
        newname = str(newnum)
    con.command("move container to workspace {}".format(newname))

def move_window_down(con, **kwargs):
    wdict = get_workspace_names(con)
    newnum = (get_current_workspace_num(con) - 10) % MAX_WORKSPACES
    if newnum in wdict:
        newname = wdict[newnum]
    else:
        newname = str(newnum)
    con.command("move container to workspace {}".format(newname))

def switch_up(con, **kwargs):
    wdict = get_workspace_names(con)
    newnum = (get_current_workspace_num(con) + 10) % MAX_WORKSPACES 
    if newnum in wdict:
        newname = wdict[newnum]
    else:
        newname = str(newnum)
    con.command("workspace {}".format(newname))

def switch_down(con, **kwargs):
    wdict = get_workspace_names(con)
    newnum = (get_current_workspace_num(con) - 10) % MAX_WORKSPACES
    if newnum in wdict:
        newname = wdict[newnum]
    else:
        newname = str(newnum)
    con.command("workspace {}".format(newname))

def move_window_lateral(con, num):
    wdict = get_workspace_names(con)
    newnum = 10*(get_current_workspace_num(con)/10) + num
    if newnum in wdict:
        newname = wdict[newnum]
    else:
        newname = str(newnum)
    con.command("move container to workspace {}".format(newname))

def switch_lateral(con, num):
    wdict = get_workspace_names(con)
    newnum = 10*(get_current_workspace_num(con)/10) + num
    if newnum in wdict:
        newname = wdict[newnum]
    else:
        newname = str(newnum)
    con.command("workspace {}".format(newname))

options = {'up' : switch_up,
        'down' : switch_down,
        'lateral' : switch_lateral,
        'mup' : move_window_up,
        'mdown' : move_window_down,
        'mlateral' : move_window_lateral,
        }

if __name__ == "__main__":
    con = Connection()
    try:
        num = int(argv[2])
    except:
        num = 0
    options[argv[1]](con, num=num)
        
    
