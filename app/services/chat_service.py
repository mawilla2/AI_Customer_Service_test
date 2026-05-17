def generate_reply(message: str) -> str:
    
    if "你好" in message:
        return "您好，请问有什么可以帮您？"
    
    return "抱歉，我暂时无法理解您的问题"