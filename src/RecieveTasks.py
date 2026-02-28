from src.classes.TaskSourceProtocol import TaskSource


def receive(source):

    if not isinstance(source, TaskSource):
        raise TypeError(
            f"Объект не реализует протокол TaskSource.")

    tasks = source.get_tasks()
    return tasks
