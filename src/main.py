from src.TaskSources import TaskGeneratorClass, FileTaskSourceClass
from RecieveTasks import receive


def main() -> None:
    tasks = []
    while (1):
        print("1 - Прочитать задачу из файла\n"
              "2 - Сгенерировтаь задачи\n"
              "3 - Увидеть задачи\n"
              "4 - exit\n")
        variant = int(input())
        if variant == 1:
            print("Укажите файл\n")
            filename = input()
            src = FileTaskSourceClass(filename)
            tasks.extend(receive(src))
        if variant == 2:
            print("Укажите количество задач\n")
            num = int(input())
            src = TaskGeneratorClass(num)
            tasks.extend(receive(src))
        if variant == 3:
            for i in range(len(tasks)):
                print(f"{tasks[i].id}: {tasks[i].payload}\n")
        if variant == 4:
            break


if __name__ == "__main__":
    main()
