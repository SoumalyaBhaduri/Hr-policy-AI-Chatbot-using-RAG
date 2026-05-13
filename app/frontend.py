import os
import streamlit as st
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
folder_path = os.path.join(BASE_DIR, "data")
os.makedirs(folder_path, exist_ok=True)

st.title("PDF Chatbot")

uploaded_file = st.file_uploader("Upload your PDF here:", type=["pdf"])
if uploaded_file is not None:
    file_path = os.path.join(folder_path, uploaded_file.name)
    with open(file_path, "wb") as out_file:
        out_file.write(uploaded_file.getbuffer())
    st.success(f"Saved file to: {file_path}")

    if st.button("Add to KnowledgeBase"):
        with st.spinner("Ingesting PDF into the knowledge base..."):
            try:
                response = requests.get("http://127.0.0.1:8000/data", timeout=120)
                if response.ok:
                    st.success("Knowledge base updated successfully.")
                else:
                    st.error(f"Ingestion failed: {response.status_code} - {response.text}")
            except requests.RequestException as exc:
                st.error(f"Failed to call ingestion endpoint: {exc}")

st.info("Chat memory is kept only for this session. Refreshing the page clears it.")

if "session_plan" not in st.session_state:
    st.session_state.session_plan = []

question = st.chat_input("Your question")
if question:
    st.session_state.session_plan.append({"role": "user", "content": question})

    payload = {"question": question}
    try:
        resp = requests.post("http://127.0.0.1:8000/chat", json=payload, timeout=30)
        if resp.ok:
            answer = resp.json().get("answer", "No answer returned.")
            st.session_state.session_plan.append({"role": "assistant", "content": answer})
        else:
            st.session_state.session_plan.append({"role": "assistant", "content": f"Error {resp.status_code}: {resp.text}"})
    except requests.RequestException as exc:
        st.session_state.session_plan.append({"role": "assistant", "content": f"Request failed: {exc}"})

for message in st.session_state.session_plan:
    st.chat_message(message["role"]).write(message["content"])
