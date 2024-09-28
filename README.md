# 🐹 My Trial Chatbot 
This is a simple chatbot application built using Streamlit and Google's Gemini Generative AI model. The chatbot, named "น้องใหม่," is an intern at Kiatnakin Phatra Bank and is designed to provide information and guidance on auto finance topics. This project is part of the study for the MADT8102 course.

## Features

- Interactive chatbot interface for user input and responses.
- Utilizes Google Generative AI's Gemini model for generating responses.
- Maintains conversation history between the user and the chatbot.
- Custom introduction message from "น้องใหม่"
- Configurable using a Gemini API key for secure AI model access.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Streamlit library installed. If not installed, use the command:
  ```bash
  pip install streamlit
  ```
- `google.generativeai` library installed. Install using:
  ```bash
  pip install google-generativeai
  ```

### Running the Application

1. **Clone the repository** (if applicable) or place the script and `README.txt` in your working directory.

2. **Install the required dependencies**:
   ```bash
   pip install streamlit google-generativeai
   ```

3. **Run the Streamlit application**:
   ```bash
   streamlit run your_script_name.py
   ```
   Replace `your_script_name.py` with the name of your Python script file.

4. The application will launch in your web browser. You will see a title and a caption mentioning "This is a part of studying MADT8102."

5. **Enter the Gemini API Key**: You will need to input a valid Gemini API Key in the provided text box to configure the chatbot. This key allows the app to interact with the Gemini model for generating responses.

6. **Interact with the Chatbot**: Once the API key is successfully configured, "น้องใหม่" will introduce herself, and you can start chatting by typing messages in the input box at the bottom.

## Code Overview

- **Gemini API Key**: The application requires a Gemini API Key, which is entered by the user to configure the generative AI model for responding to user inputs.

- **Session State**: Streamlit's session state is used to:
  - Track conversation history (`chat_history`).
  - Check if the Gemini model is configured (`gemini_configured`).
  - Determine if the introduction message has been sent (`introduction_sent`).
  - Store the model instance (`model`).

- **Introduction Message**: The chatbot sends an introduction message upon successful configuration of the Gemini model using the provided API key.

- **User Input and Bot Response**: The app captures user input, sends it to the configured Gemini model, and displays the generated response.

- **Error Handling**: Proper error messages are shown if there are issues with setting up the Gemini model or generating responses.

## Notes

- **Gemini API Key**: Make sure you have a valid API key from Google's Generative AI platform to use this application.
- **Customization**: You can customize the chatbot’s introduction message or appearance in the code as desired.

## Troubleshooting

- If you encounter errors related to the Gemini model configuration, double-check that the API key is correct and has the required permissions.
- Ensure you have internet access while running the application, as it requires connecting to the Google Generative AI API.

## License

This project is a study material for educational purposes as part of the MADT8102 course. 
