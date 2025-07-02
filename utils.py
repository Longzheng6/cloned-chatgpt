from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

def get_chat_response(prompt, memory, openai_api_key, base_url):
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       openai_api_key=openai_api_key,
                       base_url=base_url)
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
# load_dotenv()
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory, os.getenv("OPENAI_API_KEY"), "https://api.aigc369.com/v1"))
# print(get_chat_response("我上一个问题是什么？", memory, os.getenv("OPENAI_API_KEY"), "https://api.aigc369.com/v1"))