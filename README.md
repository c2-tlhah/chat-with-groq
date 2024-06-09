# AI Chat with GROQ

This project is a Streamlit web application that allows users to interact with an AI model from GROQ. The application provides a simple and intuitive interface for users to enter prompts and receive responses from the AI.

## Features
- Select different AI models to chat with.
- Enter prompts and receive real-time responses.
- Maintains a chat history for the session.
- Customizable UI with custom CSS styling.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later installed.
- Streamlit installed. If not, install it using `pip install streamlit`.
- An API key for GROQ. You can set this up in the script.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/groq-chat.git
    cd groq-chat
    ```

2. Install the necessary Python packages:

    ```bash
    pip install streamlit groq
    ```

3. Set up your API key in the script:

    Replace `your_api_key_here` with your actual API key:

    ```python
    api_key = "your_api_key_here"
    ```

## Usage

1. Navigate to the directory containing the `GROQ.py` script.

2. Run the Streamlit application:

    ```bash
    streamlit run GROQ.py
    ```

3. Open your web browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).

## Custom CSS for Styling

This line configures the Streamlit page with a title, icon, and layout. Below is the custom CSS to style the web interface:

```python
st.markdown("""
    <style>
        body { font-family: 'Arial', sans-serif; background-color: #f0f2f6; color: #333333; }
        .css-18e3th9 { padding: 2rem 1rem 2rem 1rem; }
        .css-1d391kg { text-align: center; }
        .css-6awftf, .css-6awftf:hover, .css-6awftf:active, .css-6awftf:focus {
            background-color: #4CAF50 !important; border: none !important; color: white !important; font-size: 1.1rem; padding: 0.75rem 1.5rem;
        }
        .css-6awftf span { display: none; }
        .css-1lcbmhc, .css-1lcbmhc:hover, .css-1lcbmhc:active, .css-1lcbmhc:focus {
            background-color: #4CAF50 !important; border: none !important; color: white !important; font-size: 1rem; padding: 0.5rem 1rem;
        }
        .stTextInput input { background-color: #ffffff; border: 1px solid #4CAF50; padding: 0.5rem; font-size: 1rem; width: 100%; }
        .stMarkdown h2 { color: #4CAF50; }
        .css-1k0ckh2 { display: flex; flex-direction: row; justify-content: space-between; align-items: center; }
        .css-1fcb4ut { display: flex; flex-direction: column; justify-content: space-between; align-items: flex-start; background-color: #ffffff; padding: 1rem; border-radius: 8px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); }
        .user-message { background-color: #e0e0e0; border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; }
        .ai-message { background-color: #c1e6f7; border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; }
    </style>
""", unsafe_allow_html=True)

Contributing

If you want to contribute to this project, follow these steps:

    Fork the repository.
    Create a new branch: git checkout -b feature-branch.
    Make your changes and commit them: git commit -m 'Add some feature'.
    Push to the branch: git push origin feature-branch.
    Submit a pull request.

#AI #Chatbot #Streamlit #GROQ #MachineLearning #DocumentProcessing #TechInnovation #Python #ConversationalAI #ArtificialIntelligence
