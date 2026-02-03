# 📰 AI-Powered Daily Tech Digest

A **local, privacy-first AI digest system** that fetches tech & product news, summarizes articles using a **local LLM (Ollama)**, and delivers the digest via **Email and Telegram** with **clickable article headings**.

---

## 🚀 Features

- 🔍 Fetches news from **Hacker News** and **Product Hunt**
- 🧠 Generates **150–200 word summaries** using **Ollama (local LLM)**
- 📧 Sends **HTML Email digest**
- 📲 Sends **Telegram digest** with clickable titles
- 🔗 Headings redirect to the **original article**
- 🗄️ Uses **SQLite** for storage
- 🔐 Secure configuration via `.env`

---

## 🛠️ Tech Stack

- Python 3.9+
- Ollama (Local LLM)
- SQLite
- Gmail SMTP
- Telegram Bot API

---

## ▶️ How to Run

```bash
# create virtual environment
python -m venv venv

# activate (Windows)
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run the project
python -m src.cli.run_digest
```

## 📬 Output

### Email Digest
- HTML formatted
- Clickable article titles

### Telegram Digest
- Clickable headings
- Redirects to original sources

---

## 👩‍💻 Author

**Megha Gupta**  
Junior Software Engineer  

Built to explore:
- Local LLM integration
- Backend workflows
- Debugging real-world systems
- Multi-channel delivery (Email + Telegram)

---

⭐ If you find this project useful, feel free to star the repository!

---

