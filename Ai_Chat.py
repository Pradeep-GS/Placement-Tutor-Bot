from telegram import Update
from telegram.ext import ContextTypes
from openai import OpenAI


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

user_states = {}

async def ai_trigger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_states[user_id] = "awaiting_ai_input"
    await update.message.reply_text("🧠 Send me your question, and I'll think like ChatGPT!")

async def handle_ai_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_states.get(user_id) == "awaiting_ai_input":
        user_message = update.message.text
        await update.message.reply_text("Thinking... 🤔")
        
        try:
            completion = client.chat.completions.create(
                model="openai/gpt-3.5-turbo-0613",
                messages=[{"role": "user", "content": user_message}],
                extra_headers={
                    "HTTP-Referer": "https://your-site.com",
                    "X-Title": "Placement-Tutor-Bot"          
                }
            )
            answer = completion.choices[0].message.content
            await update.message.reply_text(answer)
        except Exception as e:
            await update.message.reply_text(f"❌ Error: {str(e)}")
        print(user_states)
        user_states.pop(user_id)