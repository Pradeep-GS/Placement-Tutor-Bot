from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters 
import Commands_Text as ct
from Ai_Chat import ai_trigger, handle_ai_input

TOKEN ="8107090405:AAGM3nLx7CZncHLPq2MnWLJJXb-KwEonzQQ"
bot = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = ct.start()
    print("message start Triggering")
    await update.message.reply_text(welcome_text, parse_mode="Markdown")
    print("message start Send")

async def help_trigger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text =  ct.get_help_message()
    print("message  help Triggering")
    await update.message.reply_text(help_text, parse_mode="Markdown")
    print("message help Send")

bot.add_handler(CommandHandler("start", start))
bot.add_handler(CommandHandler("help", help_trigger))
bot.add_handler(CommandHandler("ai", ai_trigger))
bot.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_ai_input)) 

print("Bot Started")
bot.run_polling()
