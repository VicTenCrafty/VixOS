import customtkinter as ctk
from src.TTY.terminal import Terminal


def main(args, vvfs, ram, terminal):
    wm = ram["wm"]
    root = ram["root"]

    win = wm.open_window("Terminal", 600, 400)
    term = Terminal(win, vvfs)
    term.pack(fill="both", expand=True)
    return "[GUI Terminal] Launched"
