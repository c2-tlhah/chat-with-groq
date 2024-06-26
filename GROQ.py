import streamlit as st
from groq import Groq

# Set up your API key
api_key = "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"
client = Groq(api_key=api_key)

# Set up the Streamlit interface
st.set_page_config(page_title="AI Chat", page_icon=":robot_face:", layout="wide")

st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #ffffff;
            color: #333333;
        }
        .css-18e3th9 {
            padding: 2rem 1rem 2rem 1rem;
        }
        .css-1d391kg {
            text-align: center;
        }
        .css-6awftf, .css-6awftf:hover, .css-6awftf:active, .css-6awftf:focus {
            background-color: #4CAF50 !important;
            border: none !important;
            color: white !important;
            font-size: 1.1rem;
            padding: 0.75rem 1.5rem;
            border-radius: 5px;
        }
        .css-6awftf span {
            display: none;
        }
        .css-1lcbmhc, .css-1lcbmhc:hover, .css-1lcbmhc:active, .css-1lcbmhc:focus {
            background-color: #4CAF50 !important;
            border: none !important;
            color: white !important;
            font-size: 1rem;
            padding: 0.5rem 1rem;
            border-radius: 5px;
        }
        .stTextInput input {
            background-color: #f9f9f9;
            border: 1px solid #4CAF50;
            padding: 0.5rem;
            font-size: 1rem;
            width: 100%;
            border-radius: 5px;
            color: #333333; /* Ensure the text is visible */
        }
        .stMarkdown h2 {
            color: #333333;
        }
        .css-1k0ckh2 {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
        }
        .css-1fcb4ut {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-start;
            background-color: #f9f9f9;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .user-message {
            background-color: #e0f7fa;
            border-radius: 8px;
            padding: 8px 12px;
            margin-bottom: 8px;
            color: #333333;
        }
        .ai-message {
            background-color: #ffecb3;
            border-radius: 8px;
            padding: 8px 12px;
            margin-bottom: 8px;
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Chat with GROQ</h1>", unsafe_allow_html=True)

# Sidebar for model selection
st.sidebar.markdown("<h2 style='color: #4CAF50;'>Model Selection</h2>", unsafe_allow_html=True)
models = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768', 'gemma-7b-it']
model = st.sidebar.selectbox("Select a model", models)

# Initialize session state for chat history and input state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "input_key" not in st.session_state:
    st.session_state.input_key = "input_1"
if "document_content" not in st.session_state:
    st.session_state.document_content = ""

# File uploader for document
st.markdown("<h2 style='color: #4CAF50;'>Upload a document:</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])

# Function to read the uploaded file
def read_file(file):
    import PyPDF2
    import docx

    if file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page).extract_text()
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
    elif file.type == "text/plain":
        text = str(file.read(), "utf-8")
    else:
        text = ""
    return text

if uploaded_file is not None:
    st.session_state.document_content = read_file(uploaded_file)
    st.success("File uploaded successfully!")

# Input form
st.markdown("<h2 style='color: #4CAF50;'>Enter your prompt below:</h2>", unsafe_allow_html=True)
user_input = st.text_input("Prompt:", key=st.session_state.input_key, placeholder="Type your message here...")

# Display the submit button and handle its action
if st.button("Send"):
    if user_input.strip():
        with st.spinner("Waiting for AI response..."):
            try:
                # Combine document content with the user's prompt
                combined_prompt = st.session_state.document_content + "\n\n" + user_input
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": combined_prompt,
                        }
                    ],
                    model=model,
                )
                ai_response = chat_completion.choices[0].message.content

                # Append the new interaction to chat history
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                st.session_state.chat_history.append({"role": "ai", "content": ai_response})

                # Clear the input field by changing the key
                st.session_state.input_key = f"input_{len(st.session_state.chat_history)}"
                st.rerun()
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a prompt before sending.")

# Display chat history
if st.session_state.chat_history:
    st.markdown("<h2 style='color: #4CAF50;'>Chat :</h2>", unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"<div class='user-message'>{chat['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='ai-message'>{chat['content']}</div>", unsafe_allow_html=True)
else:
    st.info("Start a conversation by entering a prompt above!")
