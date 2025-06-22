import json
import os


class VVFS:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

        if os.path.exists(filename):
            self._load()
        else:
            self._create()

    def _create(self):
        self.data = {
            "system": {
                "os_name": "VixOS",
                "version": "0.1"
            },
            "files": {}
        }
        self._save()

    def _load(self):
        with open(self.filename, "r") as f:
            self.data = json.load(f)

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f)

    def read_file(self, path):
        return self.data["files"].get(path, "")

    def write_file(self, path, content):
        self.data["files"][path] = content
        self._save()

    def list_files(self):
        return list(self.data["files"].keys())
