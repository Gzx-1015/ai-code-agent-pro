from app.agents.reviewer import review_agent
from app.agents.security import security_agent
from app.agents.fixer import fix_agent
from app.core.diff import generate_patch

def process_code(file_path, code):
    review = review_agent(code)
    security = security_agent(code)

    issues = review + "\n" + security
    fixed = fix_agent(code, issues)

    patch = generate_patch(code, fixed, file_path)

    return {
        "review": review,
        "security": security,
        "patch": patch
    }
