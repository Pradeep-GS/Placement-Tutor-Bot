from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
from dotenv import load_dotenv
import os
import asyncio
from datetime import datetime, timedelta
import json
from leetcode import *
from ai import *

load_dotenv()
TOKEN = os.getenv("TOKENS")

USERS_FILE = "users.json"

if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r") as f:
        all_users = json.load(f)
else:
    all_users = []

user_states = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in all_users:
        all_users.append(chat_id)
        with open(USERS_FILE, "w") as f:
            json.dump(all_users, f)
    msg = """👋 Welcome to Placement Tutor Bot!
Daily unsolved LeetCode questions and aptitude questions will be sent to you.
You have 9 hours to answer; correct answers and tutorial links will be provided if wrong."""
    await update.message.reply_text(msg)

async def help_trigger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Use this bot to get daily coding and aptitude questions. Answer them here or ask AI questions anytime."
    await update.message.reply_text(msg)

async def trigger_leetcode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_states[chat_id] = "leetcode"
    context.user_data["problem_title"] = title()
    await update.message.reply_text("Please give your answer for today's LeetCode question:")

async def trigger_ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_states[chat_id] = "ai"
    await update.message.reply_text("Ask any question and I will answer in a professional way:")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text
    state = user_states.get(chat_id)

    if state == "leetcode":
        answer = leetcode_answer_check(context.user_data.get("problem_title"), text)
        await update.message.reply_text(answer)
        user_states[chat_id] = None
    elif state == "ai":
        answer = ask_anything(text)
        await update.message.reply_text(answer)
        user_states[chat_id] = None

async def scheduler(app, question_hour=10, question_minute=37, answer_delay_hours=9):
    while True:
        now = datetime.now()
        target_time = now.replace(hour=question_hour, minute=question_minute, second=0, microsecond=0)
        if now >= target_time:
            target_time += timedelta(days=1)
        wait_seconds = (target_time - now).total_seconds()
        await asyncio.sleep(wait_seconds)

        question_text = totelegram()
        for chat_id in all_users:
            try:
                user_states[chat_id] = "leetcode"
                context = {}
                context["problem_title"] = title()
                await app.bot.send_message(chat_id=chat_id, text=question_text)
            except Exception as e:
                print(f"Could not send to {chat_id}: {e}")

        # await asyncio.sleep(answer_delay_hours * 3600)
        await asyncio.sleep(20)
        answer_text = leetcode_answer_generator(title())
        for chat_id in all_users:
            try:
                await app.bot.send_message(chat_id=chat_id, text=answer_text)
            except Exception as e:
                print(f"Could not send to {chat_id}: {e}")

async def on_startup(app):
    app.create_task(scheduler(app))

app = ApplicationBuilder().token(TOKEN).post_init(on_startup).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_trigger))
app.add_handler(CommandHandler("answer", trigger_leetcode))
app.add_handler(CommandHandler("ai", trigger_ai))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

try:
    print("Bot Started")
    app.run_polling()
except KeyboardInterrupt:
    print("Bot Stopped")