from .models import CustomLLM_Siliconflow, embeddings_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, PyPDFDirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.runnables import RunnableParallel, RunnablePassthrough


#设置数据库
vectorstore = Chroma(
    embedding_function=embeddings_model,
    persist_directory='./db',
)


# #加载文件，并向量化
# loader = PyPDFDirectoryLoader('./files')
# docs = loader.load()
#
# text_splitter = CharacterTextSplitter(
#     separator='\n',
#     chunk_size=600,
#     chunk_overlap=100,
#     length_function=len,
#     is_separator_regex=False,
# )
#
# to_vectorstore = text_splitter.split_documents(docs)

# vectorstore.add_documents(to_vectorstore)


#设置提示词与大模型
llm = CustomLLM_Siliconflow()


prompt = ChatPromptTemplate.from_template(
    ''' 只根据以下内容进行回答：
    {context}
    
    用户输入问题为：{question}
    '''
)


#设置工作流与输出
retriever = vectorstore.as_retriever()
setup_and_retriever = RunnableParallel(
    {
        'context': retriever ,
        'question': RunnablePassthrough()
    }
)

output_parser = StrOutputParser()



chain = setup_and_retriever | prompt | llm | output_parser


#将结果传到视图函数
def process_user_message(message: str) -> str:
    bot_response = chain.invoke(message)
    return bot_response