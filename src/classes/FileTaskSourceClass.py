from classes.TaskDataclass import Task


class FileTaskSource:
    def __init__(self, filename):
        self.filename = filename

    def get_tasks(self):
        tasks = []
        with open(self.filename, 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2:
                    id = parts[0]
                    payload = parts[1]
                    tasks.append(Task(id=id, payload=payload))
        return tasks
