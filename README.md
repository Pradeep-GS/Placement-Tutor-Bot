
# 📚 Placement Tutor Telegram Bot 🎓🤖

A smart AI-powered Telegram-based learning assistant designed to help students practice coding daily, get automated feedback on solutions, and ask AI-powered doubts.

---

## 📌 Key Features

- ⏰ **Scheduled problem delivery** (Daily at 6:00 AM)  
- 🧾 **Answer submission window** until 6:00 PM via `/answer`  
- 🤖 **Automated solution review** using GPT API  
- 💬 **Instant AI doubt assistance** using `/ai`  

---

## 🚀 Planned Enhancements

- Automatic solution submission to **LeetCode**  
- Leaderboards, analytics, and personalized learning roadmap  
- Streak tracking and difficulty progression mode  

---

## 🛠️ Tech Stack

- Python  
- Telegram Bot API  
- GPT API Integration  
- Task Scheduling & Automation  

---

## ⚙️ Setup Instructions

### 1️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 2️⃣ Create a Telegram Bot & Get Token

1. Open **Telegram** and search for [@BotFather](https://t.me/BotFather).  
2. Send `/start` to BotFather and then `/newbot`.  
3. Follow the instructions to name your bot and choose a username (must end with `bot`).  
4. After creation, you will receive a **Telegram API Token**.  
5. Copy this token; it will be used as `TOKENS` in your `.env` file.

### 3️⃣ Get GPT API Key

1. Create an account on OpenAI or OpenRouter (depending on your GPT provider).  
2. Generate an API key from your account dashboard.  
3. Copy this key; it will be used as `API_KEY` in your `.env` file.

### 4️⃣ Create a `.env` File

Create a file named `.env` in your project folder with the following content:

```env
TOKENS=your_telegram_bot_token_here
API_KEY=your_gpt_api_key_here
```

> Replace `your_telegram_bot_token_here` and `your_gpt_api_key_here` with your actual keys.

### 5️⃣ Run the Bot

```bash
python bot.py
```

Your bot should now start, automatically send daily questions, evaluate answers, and respond to AI queries.

---

## 📬 Usage

- `/start` → Register and start receiving daily questions  
- `/help` → View available bot commands  
- `/answer` → Submit solution for today’s question  
- `/ai` → Ask a programming or placement-related doubt  

---

## 🎯 Purpose

This bot helps students:

- Build consistency in coding practice  
- Get AI-powered feedback instantly  
- Simulate real coding interview pressure  
- Access interactive doubt solving  

It is ideal for placement aspirants and competitive programmers aiming to improve problem-solving skills efficiently.

---

### ⭐ Contribution

Feel free to fork, suggest improvements, or contribute new features like:  

- Multi-language support  
- Dashboard for progress tracking  
- Gamified leaderboards  
