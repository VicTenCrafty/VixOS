import customtkinter as ctk
from PIL import Image, ImageTk
import os
import tkinter as tk

class DesktopEnvironment(ctk.CTkFrame):
    def __init__(self, master, wm):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.configure(fg_color="black")
        self.wm = wm
        self.master = master

        self.after(100, self.set_wallpaper)
        self.create_dock()

    def set_wallpaper(self):
        self.master.update_idletasks()
        screen_width = self.master.winfo_width()
        screen_height = self.master.winfo_height()

        wallpaper_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "wallpaper.png"))
        if os.path.exists(wallpaper_path):
            img = Image.open(wallpaper_path).resize((screen_width, screen_height), Image.LANCZOS)
            self.bg_imgtk = ImageTk.PhotoImage(img)
            self.bg_label = tk.Label(self, image=self.bg_imgtk, bd=0)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bg_label.lower()

    def create_dock(self):
        self.canvas_dock = tk.Canvas(self, height=80, bg="black", highlightthickness=0)
        self.canvas_dock.place(relx=0.5, rely=0.96, anchor="s", width=300, height=70)

        self.icon_data = [
            {"emoji": "🖥️", "name": "terminal"},
            {"emoji": "📁", "name": "files"},
            {"emoji": "🧩", "name": "notepad"},
        ]

        x = 20
        for icon in self.icon_data:
            btn = tk.Button(
                self.canvas_dock,
                text=icon["emoji"],
                font=("Segoe UI Emoji", 20),
                width=2,
                height=1,
                bd=0,
                relief="flat",
                bg="#1f1f1f",
                fg="white",
                activebackground="#333333",
                command=lambda name=icon["name"]: self.launch_app(name)
            )
            btn_window = self.canvas_dock.create_window(x, 10, anchor="nw", window=btn)
            x += 80

    def launch_app(self, app_name):
        try:
            from src.TTY.commands import run
            run([app_name], self.wm.vvfs, {"wm": self.wm, "root": self}, self.wm.terminal)
        except Exception as e:
            print(f"[DE] Failed to launch {app_name}: {e}")
