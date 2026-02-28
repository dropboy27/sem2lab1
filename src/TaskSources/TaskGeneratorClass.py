from random import randint, choice
from src.classes.TaskDataclass import Task


class TaskGenerator:
    possible_tasks = ('Do homework', 'Make dinner',
                      'Make lunch', 'Make breakfast')

    def __init__(self, tasks_number: int = 1):
        self.tasks_number = tasks_number

    def get_tasks(self):
        tasks = []
        for i in range(self.tasks_number):
            tasks.append(Task(id=randint(1, self.tasks_number*10),
                         payload=choice(self.possible_tasks)))
        return tasks
