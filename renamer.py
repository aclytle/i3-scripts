#!/usr/bin/env python2

from i3ipc import Connection
from workspacer import get_current_workspace_num, get_workspace_names
from sys import argv
import subprocess

if __name__ == "__main__":
    con = Connection()
    names = get_workspace_names(con)
    current_num = get_current_workspace_num(con)
    if current_num in names:
        current_name = names[current_num]
    else:
        current_name = current_num
    p = subprocess.Popen(["dmenu", "-p","{}:".format(current_name)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.stdin.close()
    newname = p.stdout.read().strip()
    if newname:
        con.command("rename workspace to {}:{}".format(current_num,newname))
    else:
        con.command("rename workspace to {}".format(current_num))
