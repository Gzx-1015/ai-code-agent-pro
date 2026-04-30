from app.core.llm import call_llm

def security_agent(code):
    prompt = f"检查安全问题：\n{code}"
    return call_llm(prompt)
