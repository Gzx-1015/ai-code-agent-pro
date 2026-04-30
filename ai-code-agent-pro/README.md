# AI Code Agent Pro (Champion Version)

## Run Backend
cd backend
pip install -r requirements.txt
export OPENAI_API_KEY=your_key
uvicorn app.main:app --reload

## Frontend
Open frontend/index.html in browser

## Webhook
Expose local server:
ngrok http 8000

Set GitHub webhook:
http://your-ngrok-url/webhook
