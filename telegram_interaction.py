
from telegram import Bot
from data import api_options

# Replace with your Telegram bot token
TELEGRAM_BOT_TOKEN = api_options.telegram_key
TELEGRAM_CHAT_ID = api_options.telegram_chat_id


# Function to send a message to telegram
async def send_message(message):
    # Send the listing message to Telegram
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

