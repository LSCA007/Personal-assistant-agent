# Personal Assistant Agent

A Python-based personal assistant agent with task management capabilities and extensible architecture.

## Features

- 🎯 **Task Management** - Create, update, complete, and delete tasks
- 💬 **Natural Language Processing** - Understand user requests in natural language
- 💾 **Persistent Storage** - Tasks stored locally in JSON format
- 🔌 **Extensible Architecture** - Easy to add new tools and capabilities
- 🤖 **Interactive CLI** - Command-line interface for interaction

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/LSCA007/personal-assistant-agent.git
   cd personal-assistant-agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```

5. **Add your OpenAI API key to `.env`**
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the agent:
```bash
python main.py
```

### Example Commands

```
You: create task Buy groceries
Assistant: Task created: Buy groceries (ID: 1)

You: list tasks
Assistant: Your tasks:
- ID 1: Buy groceries

You: complete task 1
Assistant: Task completed: Buy groceries

You: help
Assistant: Available tools:
- create_task: Create a new task with title, description, and optional due date
- complete_task: Mark a task as completed by its ID
- list_tasks: List all tasks
- get_task: Get details of a specific task by ID
- delete_task: Delete a task by its ID
```

## Project Structure

```
personal-assistant-agent/
├── main.py              # Entry point - Run this to start the agent
├── agent.py             # Agent logic and request routing
├── tools.py             # Tool definitions and implementations
├── tasks.py             # Task management module
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Architecture

### Components

1. **PersonalAssistantAgent** (`agent.py`)
   - Main agent class
   - Processes user input
   - Routes requests to appropriate tools
   - Maintains conversation history

2. **TaskManager** (`tasks.py`)
   - Manages task creation, completion, and deletion
   - Handles persistent storage (tasks.json)
   - Provides task retrieval and listing

3. **Tools** (`tools.py`)
   - Define available actions the agent can perform
   - Wraps TaskManager functionality
   - Extensible for new capabilities

## Extending the Agent

To add new capabilities:

1. Create a new tool function in `tools.py`
2. Add it to the `TOOLS` list
3. Add routing logic in `agent.py` (in the `process_input` method)

Example:
```python
def weather(location: str) -> str:
    """Get weather for a location."""
    # Implementation here
    return f"Weather in {location}: ..."

# Add to TOOLS list:
{
    "name": "weather",
    "description": "Get weather information for a location",
    "func": weather
}
```

## License

MIT

## Contributing

Feel free to submit issues and enhancement requests!
