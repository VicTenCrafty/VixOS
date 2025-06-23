import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
import os

class WallpaperTest(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Wallpaper Debug")

        self.after(100, self.set_wallpaper)

    def set_wallpaper(self):
        self.update_idletasks()

        width = self.winfo_width()
        height = self.winfo_height()

        path = os.path.abspath("wallpaper.png")
        print(f"[WallpaperTest] Loading image from: {path}")
        print(f"[WallpaperTest] Window size: {width}x{height}")

        if os.path.exists(path):
            img = Image.open(path).resize((width, height), Image.LANCZOS)
            print(f"[WallpaperTest] PIL image size: {img.size}")

            bg_imgtk = CTkImage(light_image=img, dark_image=img, size=(width, height))
            label = ctk.CTkLabel(self, image=bg_imgtk, text="", width=width, height=height)
            label.place(x=0, y=0)
            label.lower()
        else:
            print("Wallpaper not found.")


if __name__ == "__main__":
    app = WallpaperTest()
    app.mainloop()
