from .models import CustomLLM_Siliconflow_Qwen
from langchain_core.prompts import ChatPromptTemplate

llm = CustomLLM_Siliconflow_Qwen()

prompt = ChatPromptTemplate.from_messages([
    ('human', '请简单介绍一下{topic}')
])

chain = prompt|llm

def process_user_message(message: str) -> str:
    bot_response = chain.invoke({'topic': message})
    return bot_response