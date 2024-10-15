class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        if not isinstance(task, str) or not task.strip():
            return "Invalid task. Task must be a non-empty string."

        if task in self._tasks:
            return f"Task '{task}' already exists."

        self._tasks.append(task)
        return f"Task '{task}' added."

    def remove_task(self, task):
        if not isinstance(task, str) or not task.strip():
            return "Invalid task. Task must be a non-empty string."

        if task in self._tasks:
            self._tasks.remove(task)
            return f"Task '{task}' removed."
        else:
            return "Task not found."

    def list_tasks(self):
        return self._tasks
