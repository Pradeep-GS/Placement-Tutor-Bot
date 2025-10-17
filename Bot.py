from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from dotenv import load_dotenv
import os
import asyncio
from datetime import datetime, timedelta
from leetcode import *
import json
from ai import *
load_dotenv()
TOKEN = os.getenv("TOKENS")

USERS_FILE = "users.json"

if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r") as f:
        all_users = json.load(f)
else:
    all_users = []
wait_msg={}

# Basic Triggers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in all_users:
        all_users.append(chat_id)
        with open(USERS_FILE, "w") as f:
            json.dump(all_users, f)
    msg = """👋 *Welcome to Placement Tutor Bot!*
🚀 This bot helps you prepare for placements by sending:
🧠 Daily *unsolved LeetCode* coding questions  
📝 Daily *IndiaBix aptitude* questions  
🕘 You’ll have *9 hours* to respond — the bot checks your answers!  
🎥 If wrong, it sends the correct answer + tutorial link.
"""
    await update.message.reply_text(msg, parse_mode="Markdown")


async def help_trigger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Hello! I’m your Placement Tutor Bot 🤖. Use /ai to get today’s LeetCode question."
    await update.message.reply_text(msg, parse_mode="Markdown")

# leetcode answer recive from user and verify
async def give_answer(update:Update,context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    wait_msg[chat_id]=True
    if wait_msg.get(chat_id):
        context.user_data["problem_title"]=title()
    await update.message.reply_text("Please Give Your Answer")
async def receive_Leetcode_answer(update:Update,context:ContextTypes.DEFAULT_TYPE):
    chat_id=update.effective_chat.id
    text=update.message.text
    if wait_msg.get(chat_id):
        answer=leetcode_answer_check(context.user_data.get("problem_title"),text)
        await update.message.reply_text(answer,parse_mode="Markdown")
        wait_msg[chat_id]=False

# Questoins taking at time
async def send_daily_question(app):
    while True:
        now = datetime.now()
        target_time = now.replace(hour=23, minute=13, second=0, microsecond=0)
        if now >= target_time:
            target_time += timedelta(days=1)

        wait_seconds = (target_time - now).total_seconds()
        print(f"Waiting {wait_seconds / 60:.2f}")
        await asyncio.sleep(wait_seconds)

        question_text = totelegram()
        for chat_id in all_users:
            try:
                await app.bot.send_message(chat_id=chat_id, text=question_text)
            except Exception as e:
                print(f"Could not send to {chat_id}: {e}")

        await asyncio.sleep(5)

        answer=leetcode_answer_generator(title=title())
        for chat_id in all_users:
            try:
                await app.bot.send_message(chat_id=chat_id, text=answer , parse_mode="Markdown")
            except Exception as e:
                print(f"Could not send to {chat_id}: {e}")
      
async def on_startup(app):
    app.create_task(send_daily_question(app))

app = ApplicationBuilder().token(TOKEN).post_init(on_startup).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_trigger))
app.add_handler(CommandHandler("ai",give_answer))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,receive_Leetcode_answer))

try:
    print("Bot Started")
    app.run_polling()
except KeyboardInterrupt:
    print("Bot Stopped")
