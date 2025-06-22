import customtkinter as ctk
from src.RAM.ram import RAM
from src.TTY.commands import COMMANDS


class Terminal(ctk.CTkFrame):
    def __init__(self, master, vvfs):
        super().__init__(master)
        self.vvfs = vvfs
        self.ram = RAM()

        self.text_area = ctk.CTkTextbox(self, wrap="word", state="disabled")
        self.text_area.pack(fill="both", expand=True)

        self.input_var = ctk.StringVar()
        self.input_entry = ctk.CTkEntry(self, textvariable=self.input_var)
        self.input_entry.pack(fill="x")
        self.input_entry.bind("<Return>", self.on_enter)
        self.input_entry.focus()

        self.write("VixOS Terminal — type 'help'\n")

    def write(self, text):
        self.text_area.configure(state="normal")
        self.text_area.insert("end", text)
        self.text_area.configure(state="disabled")
        self.text_area.see("end")

    def on_enter(self, event):
        cmd = self.input_var.get().strip()
        self.write(f"> {cmd}\n")
        self.input_var.set("")

        if cmd:
            output = self.execute_command(cmd)
            self.write(output + "\n")
        return "break"

    def execute_command(self, cmd_line):
        parts = cmd_line.strip().split()
        if not parts:
            return ""
        name, *args = parts
        func = COMMANDS.get(name)
        if func:
            try:
                return func(args, self.vvfs, self.ram, self)
            except Exception as e:
                return f"[error] {str(e)}"
        return f"[VixOS] Unknown command: {name}"
