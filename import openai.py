import openai
import json
import os
from dotenv import load_dotenv
from prompts import system_prompt, test_messages
from actions import available_actions

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to execute actions
def execute_action(action: dict) -> dict:
    """
    Executes the specified function from available actions.
    Args:
        action (dict): A dictionary containing the action name and parameters.
    Returns:
        dict: The result of the executed function or an error message.
    """
    function_name = action.get("function_name")
    parameters = action.get("parameters", {})

    if function_name in available_actions:
        try:
            # Call the corresponding function with parameters
            result = available_actions[function_name](**parameters)
            return result
        except Exception as e:
            return {"error": f"Failed to execute {function_name}: {str(e)}"}
    else:
        return {"error": f"Unknown action: {function_name}"}

# Function to handle the AI ReAct loop
def agent_loop(messages: list):
    """
    Implements the ReAct loop for the AI agent.
    Args:
        messages (list): A list of conversation messages between user and assistant.
    """
    print("Starting AI agent loop...")
    while True:
        # Send messages to OpenAI API
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Replace with gpt-3.5-turbo if using that model
                messages=messages
            )
        except Exception as e:
            print(f"Error communicating with OpenAI API: {e}")
            break

        # Get the AI's response
        ai_response = response["choices"][0]["message"]["content"]
        print(f"\nAI Response:\n{ai_response}")

        # Check if the response includes an action
        if "Action" in ai_response:
            try:
                # Parse the action JSON
                action_str = ai_response.split("Action:")[1].split("PAUSE")[0].strip()
                action = json.loads(action_str)
                print(f"\nExecuting Action: {action}")

                # Execute the action and get the result
                action_result = execute_action(action)
                print(f"\nAction Result: {action_result}")

                # Append the action response to the conversation
                messages.append({"role": "assistant", "content": f"Action_Response: {action_result}"})
            except Exception as e:
                print(f"Error parsing or executing action: {e}")
                messages.append({"role": "assistant", "content": f"Error: {e}"})
        else:
            # If no action is needed, output the final answer and exit
            print("\nFinal Answer:")
            print(ai_response)
            break

# Entry point for the script
if __name__ == "__main__":
    print("AI Agent is starting...")
    try:
        # Start the agent loop with predefined test messages
        agent_loop(test_messages)
    except KeyboardInterrupt:
        print("\nExiting the AI agent.")
