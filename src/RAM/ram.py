from src.GUI.wm import WindowManager


class RAM(dict):
    def __init__(self, root=None):
        super().__init__()
        if root:
            self["wm"] = WindowManager(root)
