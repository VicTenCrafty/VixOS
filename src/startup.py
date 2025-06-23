from tkinter import Tk
import customtkinter as ctk
from src.Motherboard.boot import Motherboard


def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("VixOS Emulator")
    root.geometry("1280x720")

    system = Motherboard()
    system.power_on(root)

    root.mainloop()


if __name__ == "__main__":
    main()
