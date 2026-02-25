class FileTaskSourceError(Exception):
    pass


class FileNotFoundError(FileTaskSourceError):
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"Файл '{filename}' не найден.")
