"""Task management module for the personal assistant agent."""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class TaskManager:
    """Manages tasks for the personal assistant."""

    def __init__(self, storage_file: str = "tasks.json"):
        self.storage_file = storage_file
        self.tasks: List[Dict] = self._load_tasks()

    def _load_tasks(self) -> List[Dict]:
        """Load tasks from storage file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        return []

    def _save_tasks(self) -> None:
        """Save tasks to storage file."""
        with open(self.storage_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title: str, description: str = "", due_date: Optional[str] = None) -> Dict:
        """Add a new task."""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self._save_tasks()
        return task

    def complete_task(self, task_id: int) -> Optional[Dict]:
        """Mark a task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self._save_tasks()
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self._save_tasks()
        return True

    def list_tasks(self, completed_only: bool = False) -> List[Dict]:
        """List all tasks or only completed tasks."""
        if completed_only:
            return [t for t in self.tasks if t["completed"]]
        return self.tasks

    def get_task(self, task_id: int) -> Optional[Dict]:
        """Get a specific task by ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
