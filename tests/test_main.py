import pytest
from unittest.mock import patch
from src.main import main
from src.classes.task_dataclass import Task

def test_main_exit(capsys):
    """Выход по пункту 5."""
    with patch('builtins.input', return_value='5'):
        main()
    captured = capsys.readouterr()
    assert "exit" in captured.out.lower() or "выход" in captured.out.lower()

def test_main_add_from_generator(capsys):
    """Добавление задач через генератор (пункт 2) и просмотр (пункт 4)."""
    inputs = ['2', '2', '4', '5']
    with patch('builtins.input', side_effect=inputs):
        with patch('src.TaskSources.task_generator.TaskGenerator') as MockGen:
            instance = MockGen.return_value
            instance.get_tasks.return_value = [
                Task(id='1', payload='test1'),
                Task(id='2', payload='test2')
            ]
            main()

    captured = capsys.readouterr()
    assert '1: test1' in captured.out
    assert '2: test2' in captured.out

def test_main_add_from_api(capsys):
    """Добавление задач через API-заглушку (пункт 3) и просмотр."""
    inputs = ['3', '2', '4', '5']
    with patch('builtins.input', side_effect=inputs):
        with patch('src.TaskSources.api_task.ApiTaskSource') as MockApi:
            instance = MockApi.return_value
            instance.get_tasks.return_value = [
                Task(id='api_1', payload='data1'),
                Task(id='api_2', payload='data2')
            ]
            main()

    captured = capsys.readouterr()
    assert 'api_1: data1' in captured.out
    assert 'api_2: data2' in captured.out

def test_main_add_from_file(capsys):
    """Добавление задач из файла (пункт 1) и просмотр."""
    inputs = ['1', 'dummy.txt', '4', '5']
    with patch('builtins.input', side_effect=inputs):
        with patch('src.TaskSources.file_task.FileTaskSource') as MockFile:
            instance = MockFile.return_value
            instance.get_tasks.return_value = [Task(id='f1', payload='file_task')]
            main()

    captured = capsys.readouterr()
    assert 'f1: file_task' in captured.out

def test_main_invalid_choice(capsys):
    """Ввод неверного пункта меню (должно быть сообщение об ошибке)."""
    inputs = ['99', '5']
    with patch('builtins.input', side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert 'неверный пункт меню' in captured.out.lower()