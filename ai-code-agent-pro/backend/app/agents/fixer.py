from app.core.llm import call_llm

def fix_agent(code, issues):
    prompt = f"修复代码:\n{code}\n问题:{issues}"
    return call_llm(prompt, temperature=0)
