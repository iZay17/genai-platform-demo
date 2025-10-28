# genai-platform-demo
# 🧠 Mini GenAI Platform Demo

A lightweight proof-of-concept for a **Generative AI Platform** built with Python, OpenAI API, and GitHub Actions.

---

## 🚀 Features

- **Generative AI microservice:** simple `/generate` endpoint that calls OpenAI GPT.
- **Governance:** logs every user prompt, timestamp, and token count.
- **DevOps Ready:** includes GitHub Actions for CI/CD linting and testing.
- **Security:** environment variables stored in `.env` file.
- **Extensible:** easily containerized and scalable to multi-cloud.

---

## 🧩 Setup Instructions

1. Clone the repo:
   
   ```bash
   git clone https://github.com/YOUR-USERNAME/genai-platform-demo.git
   cd genai-platform-demo
3. Install dependencies:
   
   pip install -r requirements.txt
4. Copy .env.example to .env and set your OpenAI API key.
   
5. Run the app:
   
   python app.py
6. Test in Postman or curl:
   
   curl -X POST http://127.0.0.1:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a haiku about AI"}'

