# ChatGPT Terminal

ChatGPT Terminal is a command-line interface application that allows users to interact with the OpenAI GPT model for assistance with various tasks, including executing terminal commands and system management. The application integrates with the user's operating system and package manager to provide tailored assistance based on the user's environment.

## Features

- Seamless integration with the user's operating system and package manager.
- Ability to execute terminal commands directly from the application.
- Secure handling of API keys and sensitive information.
- Can read contents of text files when prompted.
- Retrieves AI-generated responses from OpenAI's GPT model using the OpenAI API.

## How to Use

1. Set up an OpenAI API key. Visit https://beta.openai.com/signup/ to sign up and get an API key if you don't already have one.

2. Put the application chaterm in your path.

3. Run the application by typing:

chaterm

4. Enter your OpenAI API key when prompted. The key will be securely stored for future use.

5. Start interacting with ChatGPT by typing your questions or requests in the terminal.

6. To exit the application, type "exit" or "quit".

## Known Shortcomings

- ChatGPT's responses can sometimes be irrelevant or repetitive.
- The application might not understand complex or ambiguous user input.
- Currently, only supports reading text files.
- The application assumes that the user has a package manager installed, which might not always be the case.
- The support for various operating systems and package managers is limited.
- May not handle edge cases in terminal commands or system management tasks.
- Direct execution of commands without user confirmation may present security risks.

## Contributing

Contributions are welcome! If you have ideas for new features, bug fixes, or improvements, please submit an issue or pull request on the GitHub repository.

## License

This project is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
