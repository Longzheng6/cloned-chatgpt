import streamlit as st
from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

st.title("💡 克隆ChatGPT")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API Key：", type="password")
    base_url = st.text_input("请输入base_url：")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "oi 小鬼，我是你的AI助手，有什么可以帮你的吗"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入你的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"], openai_api_key, base_url)

    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)