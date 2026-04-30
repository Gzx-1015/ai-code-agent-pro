from fastapi import APIRouter, Request
from app.worker import process_code
from app.services.github import comment_pr

router = APIRouter()

GITHUB_TOKEN = "REPLACE_WITH_YOUR_TOKEN"

@router.post("/webhook")
async def github_webhook(req: Request):
    data = await req.json()

    if "pull_request" not in data:
        return {"msg": "ignored"}

    repo = data["repository"]["full_name"]
    pr_number = data["pull_request"]["number"]

    # Demo code (replace with real PR diff fetch)
    code = "def add(a,b): return a+b\nprint(add(1))"

    result = process_code("pr_file.py", code)

    comment_body = f"""
## 🤖 AI Code Review

### 🔍 Review
{result["review"]}

### 🔐 Security
{result["security"]}

### 🛠 Patch
```diff
{result["patch"]}
```
"""

    comment_pr(repo, pr_number, GITHUB_TOKEN, comment_body)

    return {"status": "commented"}
