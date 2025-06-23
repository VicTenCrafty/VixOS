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

        from src.GUI.wm import WindowManager
        from src.GUI.DE import DesktopEnvironment

        wm = WindowManager(root)
        self.de = DesktopEnvironment(root, wm, self.vvfs, fake_terminal)
        # Fake terminal setup for launching apps
        from src.TTY.terminal import Terminal
        fake_terminal = Terminal(root, self.vvfs)
        fake_terminal.ram["root"] = root
        fake_terminal.ram["wm"] = wm

        from src.Apps import terminal as term_app
        term_app.main([], self.vvfs, fake_terminal.ram, fake_terminal)


