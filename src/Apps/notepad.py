import customtkinter as ctk


def main(args, vvfs, ram, terminal):
    filename = args[0] if args else "untitled.txt"
    wm = ram["wm"]

    content_frame = wm.open_window(f"Notepad - {filename}", width=500, height=400)

    textbox = ctk.CTkTextbox(content_frame, wrap="word")
    textbox.pack(fill="both", expand=True, padx=10, pady=10)
    textbox.insert("1.0", vvfs.read_file(filename))

    def save():
        vvfs.write_file(filename, textbox.get("1.0", "end-1c"))
        terminal.write(f"[Notepad] Saved {filename}\n")

    ctk.CTkButton(content_frame, text="Save", command=save).pack(pady=6)

    return f"[GUI Notepad] Opened {filename}"
