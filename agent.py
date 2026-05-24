"""Personal assistant agent implementation."""

import os
from dotenv import load_dotenv
from tools import TOOLS

# Load environment variables
load_dotenv()


class PersonalAssistantAgent:
    """Main agent class for personal assistance."""

    def __init__(self):
        """Initialize the agent."""
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set in environment variables")
        
        self.tools = {tool["name"]: tool["func"] for tool in TOOLS}
        self.conversation_history = []

    def process_input(self, user_input: str) -> str:
        """
        Process user input and determine the appropriate action.
        
        Args:
            user_input: The user's request
            
        Returns:
            The agent's response
        """
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Simple routing logic based on keywords
        user_input_lower = user_input.lower()
        
        if "create task" in user_input_lower or "add task" in user_input_lower:
            return self._handle_create_task(user_input)
        elif "complete task" in user_input_lower or "done" in user_input_lower:
            return self._handle_complete_task(user_input)
        elif "list tasks" in user_input_lower or "show tasks" in user_input_lower:
            return self.tools["list_tasks"]()
        elif "delete task" in user_input_lower or "remove task" in user_input_lower:
            return self._handle_delete_task(user_input)
        else:
            return self._default_response(user_input)

    def _handle_create_task(self, user_input: str) -> str:
        """Handle task creation requests."""
        # Extract task details from input (simple parsing)
        parts = user_input.split(",")
        title = parts[0].replace("create task", "").replace("add task", "").strip()
        description = parts[1].strip() if len(parts) > 1 else ""
        due_date = parts[2].strip() if len(parts) > 2 else ""
        
        return self.tools["create_task"](title, description, due_date)

    def _handle_complete_task(self, user_input: str) -> str:
        """Handle task completion requests."""
        # Extract task ID from input
        import re
        match = re.search(r'\d+', user_input)
        if match:
            task_id = int(match.group())
            return self.tools["complete_task"](task_id)
        return "Please specify a task ID to complete."

    def _handle_delete_task(self, user_input: str) -> str:
        """Handle task deletion requests."""
        # Extract task ID from input
        import re
        match = re.search(r'\d+', user_input)
        if match:
            task_id = int(match.group())
            return self.tools["delete_task"](task_id)
        return "Please specify a task ID to delete."

    def _default_response(self, user_input: str) -> str:
        """Provide a default response."""
        return (
            "I'm your personal assistant. I can help you with:\n"
            "- Creating tasks (e.g., 'create task Buy groceries')\n"
            "- Completing tasks (e.g., 'complete task 1')\n"
            "- Listing tasks (e.g., 'list tasks')\n"
            "- Deleting tasks (e.g., 'delete task 1')\n\n"
            "What would you like me to help with?"
        )

    def get_available_tools(self) -> str:
        """Get a description of available tools."""
        tools_desc = "Available tools:\n"
        for tool in TOOLS:
            tools_desc += f"- {tool['name']}: {tool['description']}\n"
        return tools_desc
