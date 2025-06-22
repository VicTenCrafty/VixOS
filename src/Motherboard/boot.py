from src.RAM.ram import RAM
from src.TTY.terminal import Terminal

class Motherboard:
    def __init__(self):
        print("[Motherboard] Initializing...")
        from src.Storage.vvfs import VVFS
        from src.GUI.display import Display

        self.vvfs = VVFS("internalstorage.vvfs")
        self.display = Display(self.vvfs)
        self.terminal = None

    def power_on(self, root):
        print("[Motherboard] Powering on VixOS...")
        self.display.boot_sequence()

        self.terminal = Terminal(root, self.vvfs)
        self.terminal.ram = RAM(root)
        self.terminal.ram["root"] = root

        self.terminal.pack(fill="both", expand=True)

