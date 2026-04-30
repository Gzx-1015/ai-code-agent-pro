import requests

def comment_pr(repo, pr_number, token, body):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {"Authorization": f"token {token}"}
    requests.post(url, json={"body": body}, headers=headers)
