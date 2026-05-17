import os
from openai import OpenAI
from openai import RateLimitError
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_ai_reply(message: str) -> str:

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "你是一个专业AI客服"
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        content = response.choices[0].message.content

        if content is None:
            return "AI没有返回内容"

        return content

    except RateLimitError:
        return "当前AI服务额度不足，请稍后再试"

    except Exception as e:
        return f"发生错误: {str(e)}"