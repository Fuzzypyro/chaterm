import openai
import json
import os
import subprocess
from getpass import getpass

def get_all_executables_in_path():
    executables = set()
    for path_dir in os.environ['PATH'].split(os.pathsep):
        if os.path.exists(path_dir):
            for entry in os.listdir(path_dir):
                entry_path = os.path.join(path_dir, entry)
                if os.path.isfile(entry_path) and os.access(entry_path, os.X_OK):
                    executables.add(entry)
    return executables

# Function to call the OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

# Initialize conversation history
conversation_history = ""

# Get all executables in PATH
executables_in_path = get_all_executables_in_path()

# Set up OpenAI API
config_dir = os.path.expanduser('~/.config/chaterm')
os.makedirs(config_dir, exist_ok=True)
api_key_file = os.path.join(config_dir, 'api_key.conf')

if not os.path.isfile(api_key_file):
    api_key = getpass('Enter your OpenAI API key: ')
    with open(api_key_file, 'w') as f:
        f.write(api_key)
    os.chmod(api_key_file, 0o600)
else:
    with open(api_key_file, 'r') as f:
        api_key = f.read().strip()

openai.api_key = api_key

print('ChatGPT Terminal (Type "exit" or "quit" to end)\n')

while True:
    # User input
    user_input = input('You: ').strip()
    if user_input.lower() in ['exit', 'quit']:
        break

    user_command = user_input.split()[0]

    if user_command in executables_in_path:
        try:
            output = subprocess.check_output(user_input, shell=True, text=True, stderr=subprocess.STDOUT)
            print(f'Terminal: {output}')
        except subprocess.CalledProcessError as e:
            error_message = f'Error: {e.output}'
            print(f'Terminal: {error_message}')
        except Exception as e:
            error_message = f'Error: Unable to execute command'
            print(f'Terminal: {error_message}')
    else:
        conversation_history += f'User: {user_input}\n'

        # Generate prompt for ChatGPT
        prompt = f"User asked the AI to perform a terminal command: {user_input}\n{conversation_history}"
        prompt += "Please provide a command to execute in the terminal for the given task. Do not provide explanations, just the command."

        # Get ChatGPT response
        chatgpt_response = generate_response(prompt)
        conversation_history += f'{chatgpt_response}\n'

        # Print the response
        print(f'{chatgpt_response}')

        if chatgpt_response.strip():  # Add this line to check if the response is not empty
            response_command = chatgpt_response.split()[0]
            if response_command in executables_in_path:
                while True:
                    confirm = input('Confirm: Do you want to execute the command? (y/n) ')
                    if confirm.lower() in ['', 'y', 'yes']:
                        try:
                            output = subprocess.check_output(chatgpt_response, shell=True, text=True, stderr=subprocess.STDOUT)
                            print(f'Terminal: {output}')
                            break
                        except subprocess.CalledProcessError as e:
                            error_message = f'Error: {e.output}'
                            print(f'Terminal: {error_message}')
                            break
                        except Exception as e:
                            error_message = f'Error: Unable to execute command'
                            print(f'Terminal: {error_message}')
                            break
                    elif confirm.lower() in ['n', 'no']:
                        break
