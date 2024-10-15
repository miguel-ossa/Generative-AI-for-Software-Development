from taskManager import TaskManager
import unittest

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task_valid(self):
        result = self.task_manager.add_task("Comprar leche")
        self.assertEqual(result, "Task 'Comprar leche' added.")
        self.assertIn("Comprar leche", self.task_manager.list_tasks())

    def test_add_task_empty(self):
        result = self.task_manager.add_task("")
        self.assertEqual(result, "Invalid task. Task must be a non-empty string.")
        self.assertNotIn("", self.task_manager.list_tasks())

    def test_add_task_none(self):
        result = self.task_manager.add_task(None)
        self.assertEqual(result, "Invalid task. Task must be a non-empty string.")
        self.assertNotIn(None, self.task_manager.list_tasks())

    def test_add_task_duplicate(self):
        self.task_manager.add_task("Comprar leche")
        result = self.task_manager.add_task("Comprar leche")
        self.assertEqual(result, "Task 'Comprar leche' already exists.")
        self.assertEqual(self.task_manager.list_tasks().count("Comprar leche"), 1)

    def test_remove_task_valid(self):
        self.task_manager.add_task("Comprar leche")
        result = self.task_manager.remove_task("Comprar leche")
        self.assertEqual(result, "Task 'Comprar leche' removed.")
        self.assertNotIn("Comprar leche", self.task_manager.list_tasks())

    def test_remove_task_not_found(self):
        result = self.task_manager.remove_task("Hacer ejercicio")
        self.assertEqual(result, "Task not found.")
        self.assertNotIn("Hacer ejercicio", self.task_manager.list_tasks())

    def test_remove_task_empty(self):
        result = self.task_manager.remove_task("")
        self.assertEqual(result, "Invalid task. Task must be a non-empty string.")
        self.assertNotIn("", self.task_manager.list_tasks())

    def test_remove_task_none(self):
        result = self.task_manager.remove_task(None)
        self.assertEqual(result, "Invalid task. Task must be a non-empty string.")
        self.assertNotIn(None, self.task_manager.list_tasks())

    def test_list_tasks_empty(self):
        self.assertEqual(self.task_manager.list_tasks(), [])

    def test_list_tasks_with_entries(self):
        self.task_manager.add_task("Comprar leche")
        self.task_manager.add_task("Llamar al médico")
        self.assertEqual(self.task_manager.list_tasks(), ["Comprar leche", "Llamar al médico"])


if __name__ == '__main__':
    unittest.main()
