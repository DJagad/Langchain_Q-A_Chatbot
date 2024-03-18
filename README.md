# Q&A Chatbot

This repository contains code for a simple question and answer (Q&A) chatbot built using Streamlit and the langchain library. The chatbot utilizes OpenAI's GPT-3.5 model for generating responses.

## Setup

To run this chatbot, you'll need to have Python installed on your machine. Follow these steps to set up the environment:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_repository
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your OpenAI API key by creating a `.env` file in the root directory of the project and adding your API key:

    ```plaintext
    OPEN_API_KEY=your_openai_api_key
    ```

## Usage

Run the following command to start the Streamlit app:

```bash
streamlit run chatbot.py
