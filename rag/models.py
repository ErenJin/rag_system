from openai import OpenAI

# API密钥, 先用明码，后面再改
API_KEY = "sk-zcfvpcipdfrizayqqkycwgrfhfrgotjkpbxbwiuftdpfayiz"


# 自定义硅基流动大模型类--逻辑推理模型
class CustomLLM_Siliconflow_Qwen:
    def __call__(self, prompt: str) -> str:
        # 初始化OpenAI客户端（base_url是硅基流动网站的地址）
        client = OpenAI(api_key=API_KEY, base_url="https://api.siliconflow.cn/v1")

        # 发送请求到模型
        response = client.chat.completions.create(
            model='THUDM/GLM-4-9B-0414',
            messages=[
                {'role': 'user',
                 'content': f"{prompt}"}  # 用户输入的提示
            ],
        )

        # 打印响应结构，以便调试
        # print("Response structure:", response)

        # 收集所有响应内容
        content = ""
        if hasattr(response, 'choices') and response.choices:
            for choice in response.choices:
                if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
                    chunk_content = choice.message.content
                    # print(chunk_content, end='')  # 可选：打印内容
                    content += chunk_content  # 将内容累加到总内容中
        else:
            raise ValueError("Unexpected response structure")

        return content  # 返回最终的响应内容


# 自定义硅基流动大模型类--逻辑推理模型
class CustomLLM_Siliconflow_bge_m3:
    def __call__(self, prompt: str) -> str:
        # 初始化OpenAI客户端（base_url是硅基流动网站的地址）
        client = OpenAI(api_key=API_KEY, base_url="https://api.siliconflow.cn/v1")

        # 发送请求到模型
        response = client.chat.completions.create(
            model='BAAI/bge-m3',
            messages=[
                {'role': 'user',
                 'content': f"{prompt}"}  # 用户输入的提示
            ],
        )

        # 打印响应结构，以便调试
        # print("Response structure:", response)

        # 收集所有响应内容
        content = ""
        if hasattr(response, 'choices') and response.choices:
            for choice in response.choices:
                if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
                    chunk_content = choice.message.content
                    # print(chunk_content, end='')  # 可选：打印内容
                    content += chunk_content  # 将内容累加到总内容中
        else:
            raise ValueError("Unexpected response structure")

        return content  # 返回最终的响应内容