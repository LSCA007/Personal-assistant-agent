"""Tool definitions for the personal assistant agent."""

from typing import Any
from tasks import TaskManager

task_manager = TaskManager()


def create_task(title: str, description: str = "", due_date: str = "") -> str:
    """Create a new task."""
    task = task_manager.add_task(title, description, due_date if due_date else None)
    return f"Task created: {task['title']} (ID: {task['id']})"


def complete_task(task_id: int) -> str:
    """Mark a task as completed."""
    task = task_manager.complete_task(task_id)
    if task:
        return f"Task completed: {task['title']}"
    return f"Task with ID {task_id} not found"


def list_tasks() -> str:
    """List all tasks."""
    tasks = task_manager.list_tasks()
    if not tasks:
        return "No tasks found."
    
    task_list = "\n".join([
        f"- ID {t['id']}: {t['title']} {'(COMPLETED)' if t['completed'] else ''}"
        for t in tasks
    ])
    return f"Your tasks:\n{task_list}"


def get_task(task_id: int) -> str:
    """Get details of a specific task."""
    task = task_manager.get_task(task_id)
    if task:
        return f"Task {task_id}: {task['title']}\nDescription: {task['description']}\nDue: {task['due_date']}"
    return f"Task with ID {task_id} not found"


def delete_task(task_id: int) -> str:
    """Delete a task."""
    if task_manager.delete_task(task_id):
        return f"Task with ID {task_id} deleted"
    return f"Task with ID {task_id} not found"


# Define tools for the agent
TOOLS = [
    {
        "name": "create_task",
        "description": "Create a new task with title, description, and optional due date",
        "func": create_task
    },
    {
        "name": "complete_task",
        "description": "Mark a task as completed by its ID",
        "func": complete_task
    },
    {
        "name": "list_tasks",
        "description": "List all tasks",
        "func": list_tasks
    },
    {
        "name": "get_task",
        "description": "Get details of a specific task by ID",
        "func": get_task
    },
    {
        "name": "delete_task",
        "description": "Delete a task by its ID",
        "func": delete_task
    }
]
