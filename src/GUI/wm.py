import customtkinter as ctk


class Window(ctk.CTkFrame):
    def __init__(self, parent, title="Window", width=400, height=300):
        super().__init__(parent, width=width, height=height, corner_radius=10, fg_color="#2a2a2a")
        self.place(x=100, y=100)
        self._drag_start = None
        self._original_geom = {"x": 100, "y": 100, "width": width, "height": height}
        self._minimized = False
        self._maximized = False
        self._parent = parent

        # Topbar
        self.topbar = ctk.CTkFrame(self, height=32, fg_color="#1f1f1f", corner_radius=10)
        self.topbar.pack(fill="x", side="top")

        # Bind drag to all children of topbar
        self.topbar.bind("<Button-1>", self.start_move)
        self.topbar.bind("<B1-Motion>", self.do_move)

        # Title
        self.title_label = ctk.CTkLabel(self.topbar, text=title, font=("Consolas", 14))
        self.title_label.pack(side="left", padx=10)
        self.title_label.bind("<Button-1>", self.start_move)
        self.title_label.bind("<B1-Motion>", self.do_move)

        # Control buttons
        self.close_btn = ctk.CTkButton(self.topbar, text="✕", width=30, height=24, fg_color="red", command=self.destroy)
        self.close_btn.pack(side="right", padx=2, pady=4)

        self.max_btn = ctk.CTkButton(self.topbar, text="⬜", width=30, height=24, command=self.toggle_maximize)
        self.max_btn.pack(side="right", padx=2, pady=4)

        self.min_btn = ctk.CTkButton(self.topbar, text="_", width=30, height=24, command=self.toggle_minimize)
        self.min_btn.pack(side="right", padx=2, pady=4)

        # Content area
        self.content = ctk.CTkFrame(self, fg_color="#2a2a2a")
        self.content.pack(fill="both", expand=True, padx=6, pady=(0, 6))

    def start_move(self, event):
        self._drag_start = (event.x_root, event.y_root, self.winfo_x(), self.winfo_y())

    def do_move(self, event):
        if not self._drag_start or self._maximized:
            return

        x_root, y_root, start_x, start_y = self._drag_start
        dx = event.x_root - x_root
        dy = event.y_root - y_root

        new_x = start_x + dx
        new_y = start_y + dy

        # Clamp to parent window
        max_x = self._parent.winfo_width() - self.winfo_width()
        max_y = self._parent.winfo_height() - self.winfo_height()
        new_x = max(0, min(new_x, max_x))
        new_y = max(0, min(new_y, max_y))

        self.place(x=new_x, y=new_y)

    def toggle_minimize(self):
        if self._minimized:
            self.content.pack(fill="both", expand=True, padx=6, pady=(0, 6))
            self._minimized = False
        else:
            self.content.forget()
            self._minimized = True

    def toggle_maximize(self):
        if not self._maximized:
            self._original_geom.update({
                "x": self.winfo_x(),
                "y": self.winfo_y(),
                "width": self.winfo_width(),
                "height": self.winfo_height(),
            })

            # Force full screen position and stretch
            self.place_forget()
            self.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
            self._maximized = True
            self.lift()
        else:
            self.place_forget()
            self.place(
                x=self._original_geom["x"],
                y=self._original_geom["y"]
            )
            self.configure(
                width=self._original_geom["width"],
                height=self._original_geom["height"]
            )
            self._maximized = False


class WindowManager:
    def __init__(self, root):
        self.root = root
        self.windows = []

    def open_window(self, title, width, height):
        win = Window(self.root, title=title, width=width, height=height)
        self.windows.append(win)
        return win.content  # You can pack your UI stuff into this!
