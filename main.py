import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Отримай токен з оточення
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Адмінський Telegram ID
ADMIN_ID = 468440691  # заміни на свій Telegram ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = context.args
    product = " ".join(args) if args else "невідомий товар"

    # Повідомлення для користувача
    await update.message.reply_text(
        f"🎣 Вас зацікавив товар: {product}\nНапишіть нижче своє питання або замовлення 👇"
    )

    # Повідомлення адміну
    if ADMIN_ID:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🔔 @{user.username or user.first_name} зацікавився товаром: {product}"
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущено...")
    app.run_polling()
