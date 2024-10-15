import pytest
from taskManager import TaskManager

@pytest.fixture
def task_manager():
    return TaskManager()

def test_add_task_valid(task_manager):
    result = task_manager.add_task("Comprar leche")
    assert result == "Task 'Comprar leche' added."
    assert "Comprar leche" in task_manager.list_tasks()

def test_add_task_empty(task_manager):
    result = task_manager.add_task("")
    assert result == "Invalid task. Task must be a non-empty string."
    assert "" not in task_manager.list_tasks()

def test_add_task_none(task_manager):
    result = task_manager.add_task(None)
    assert result == "Invalid task. Task must be a non-empty string."
    assert None not in task_manager.list_tasks()

def test_add_task_duplicate(task_manager):
    task_manager.add_task("Comprar leche")
    result = task_manager.add_task("Comprar leche")
    assert result == "Task 'Comprar leche' already exists."
    assert task_manager.list_tasks().count("Comprar leche") == 1

def test_remove_task_valid(task_manager):
    task_manager.add_task("Comprar leche")
    result = task_manager.remove_task("Comprar leche")
    assert result == "Task 'Comprar leche' removed."
    assert "Comprar leche" not in task_manager.list_tasks()

def test_remove_task_not_found(task_manager):
    result = task_manager.remove_task("Hacer ejercicio")
    assert result == "Task not found."
    assert "Hacer ejercicio" not in task_manager.list_tasks()

def test_remove_task_empty(task_manager):
    result = task_manager.remove_task("")
    assert result == "Invalid task. Task must be a non-empty string."
    assert "" not in task_manager.list_tasks()

def test_remove_task_none(task_manager):
    result = task_manager.remove_task(None)
    assert result == "Invalid task. Task must be a non-empty string."
    assert None not in task_manager.list_tasks()

def test_list_tasks_empty(task_manager):
    assert task_manager.list_tasks() == []

def test_list_tasks_with_entries(task_manager):
    task_manager.add_task("Comprar leche")
    task_manager.add_task("Llamar al médico")
    assert task_manager.list_tasks() == ["Comprar leche", "Llamar al médico"]
