from src.classes.TaskDataclass import Task
from src.exceptions.FileTaskSourceExceptions import FileNotFoundError


class FileTaskSource:
    def __init__(self, filename):
        self.filename = filename

    def get_tasks(self):
        tasks = []
        if not f:
            raise FileNotFoundError(self.filename)
        with open(self.filename, 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2:
                    id = parts[0]
                    payload = parts[1]
                    tasks.append(Task(id=id, payload=payload))
        return tasks
