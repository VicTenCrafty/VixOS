import importlib


def echo(args, vvfs, ram, terminal):
    return ' '.join(args)


def help_cmd(args, vvfs, ram, terminal):
    lines = [
        "Available commands:",
        "  echo [text]         - print text",
        "  help                - show this help message",
        "  about               - info about VixOS",
        "  version             - show OS version",
        "  ls / dir            - list VVFS files",
        "  touch [file]        - create file",
        "  nano [file]         - stub editor",
        "  cat [file]          - print file content",
        "  run [app] [args...] - launch TTY or GUI app",
        "  loadvvfs [file]     - switch to different .vvfs file"
    ]
    return "\n".join(lines)


def about(args, vvfs, ram, terminal):
    return "VixOS - A Fake Python OS for Fun and Profit."


def version(args, vvfs, ram, terminal):
    return vvfs.data["system"].get("version", "Unknown")


def ls(args, vvfs, ram, terminal):
    return '\n'.join(vvfs.list_files()) or "No files found."


def dir_cmd(args, vvfs, ram, terminal):
    return ls(args, vvfs, ram, terminal)


def touch(args, vvfs, ram, terminal):
    if not args:
        return "Usage: touch [filename]"
    filename = args[0]
    vvfs.write_file(filename, "")
    return f"Created empty file: {filename}"


def nano(args, vvfs, ram, terminal):
    if not args:
        return "Usage: nano <filename>"
    filename = args[0]
    vvfs.write_file(filename, "[Empty file edited in nano]")
    return f"Fake-edited {filename}"


def cat(args, vvfs, ram, terminal):
    if not args:
        return "Usage: cat <filename>"
    filename = args[0]
    content = vvfs.read_file(filename)
    return content if content else f"File '{filename}' is empty or does not exist."


def loadvvfs(args, vvfs, ram, terminal):
    if not args:
        return "Usage: loadvvfs <filename.vvfs>"
    filepath = args[0]
    try:
        from src.Storage.vvfs import VVFS
        terminal.vvfs = VVFS(filepath)
        return f"Switched to VVFS file: {filepath}"
    except Exception as e:
        return f"Failed to load VVFS: {e}"


def run(args, vvfs, ram, terminal):
    if not args:
        return "Usage: run <app> [args]"
    app_name, *app_args = args

    if app_name == "notepad":
        import Apps.notepad as app_module
    else:
        try:
            app_module = importlib.import_module(f"Apps.{app_name}")
        except Exception as e:
            return f"Error running app '{app_name}': {e}"

    result = app_module.main(app_args, vvfs, ram, terminal)
    terminal.active_app = None  # GUI app, no input needed here
    return result


COMMANDS = {
    "echo": echo,
    "help": help_cmd,
    "about": about,
    "version": version,
    "ls": ls,
    "dir": dir_cmd,
    "touch": touch,
    "nano": nano,
    "cat": cat,
    "loadvvfs": loadvvfs,
    "run": run,
}
