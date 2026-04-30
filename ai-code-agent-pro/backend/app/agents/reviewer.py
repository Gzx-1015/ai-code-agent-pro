from app.core.llm import call_llm

def review_agent(code):
    prompt = f"检查代码问题：\n{code}"
    return call_llm(prompt)
