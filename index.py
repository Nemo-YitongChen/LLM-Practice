import os, time
from openai import OpenAI

# 加载 .env 到环境变量
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# 配置 OpenAI 服务

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

def get_completion(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )
    return response.choices[0].message.content

# 任务描述
instruction = """
Your task is to proofread and revise the following paragraph in proper grammar, commonly used words, and short sentences.

You should revise the paragraph according to user defined purpose. If no purpose defined, the purpose would be "improve readability and suitability for workplace".

You should not change the meaning of the paragraph and you will chose the best one from the choices.
"""

# 用户输入
while(True):
    paragraph=input("\n\nPlease input the paragraph: \n\n")
    purpose=input("\n\nWhat's the purpose of this revision? \n\n")
    
    input_text = f"""
    Purpose: {purpose}

    Paragraph: {paragraph}
    """

    # prompt 模版。instruction 和 input_text 会被替换为上面的内容
    prompt = f"""
    {instruction}

    User Input:
    {input_text}
    """

    # 调用大模型
    response = get_completion(prompt)
    print("response: \n\n",response)

    time.sleep(2)
