import streamlit as st
from main_pipeline import run_pipeline

st.set_page_config(
    page_title="School Information Chatbot",
    page_icon="🏫",
    layout="centered"
)

st.markdown("""
<style>
.chat-box {
    background-color: #111;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.user {
    color: #4da6ff;
    font-weight: bold;
}
.bot {
    color: #7CFC00;
}
.footer {
    text-align: center;
    margin-top: 30px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.title("🏫 School Information Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

question = st.text_input("Ask your question")

if st.button("Send") and question:
    answer = run_pipeline(question)
    st.session_state.chat.append(("You", question))
    st.session_state.chat.append(("Bot", answer))

for role, msg in st.session_state.chat:
    if role == "You":
        st.markdown(f"<div class='chat-box user'>You: {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-box bot'>Bot: {msg}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by Sarfraz Khan</div>", unsafe_allow_html=True)





"""What are the school fees?
Primary class fees
Secondary fees
School timing
Where is the school located?
Admission process
Is transport facility available?
What is the name of the school?
Where is the school located?
What is the school timing?
What are the fees for primary classes?
What curriculum does the school follow?
You earlier asked about fees. 
Do you want admission details?
Can you provide the admission process?
What is the name of the school?
Where is the school located?
What is the school timing?
What are the fees for primary classes?
What curriculum does the school follow?
"""
