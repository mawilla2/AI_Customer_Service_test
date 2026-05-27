from openai import OpenAI, RateLimitError

from app.core.config import settings


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_ai_reply(message: str) -> str:

    try:

        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "你是一个专业的 AI 客服"
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        content = response.choices[0].message.content

        if content is None:
            return "AI 没有返回内容"

        return content

    except RateLimitError:
        return "当前 AI 服务额度不足，请稍后再试"

    except Exception as e:
        return f"发生错误: {str(e)}"
