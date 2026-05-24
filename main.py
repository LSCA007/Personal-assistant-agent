"""Main entry point for the personal assistant agent."""

from agent import PersonalAssistantAgent


def main():
    """Run the personal assistant agent."""
    print("🤖 Personal Assistant Agent")
    print("=" * 50)
    print("Type 'help' for available commands or 'quit' to exit.\n")
    
    try:
        agent = PersonalAssistantAgent()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please set up your .env file with OPENAI_API_KEY")
        return
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "quit":
                print("Goodbye!")
                break
            
            if user_input.lower() == "help":
                print("\n" + agent.get_available_tools())
                continue
            
            response = agent.process_input(user_input)
            print(f"\nAssistant: {response}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
