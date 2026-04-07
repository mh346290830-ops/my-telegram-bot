import telebot
import google.generativeai as genai

# এখানে আপনার সঠিক টোকেন এবং কী দিন
TELEGRAM_TOKEN = "8651980061:AAGU50lPJ3NDSzXxBOw0O2INKOp2zymsLAU" 
GEMINI_API_KEY = "AIzaSyB5zLjJ6KZwqNZ8Bsr6cDL7xtUwGrc6YJ0"

# Gemini Setup (Model Name Updated)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro') # এখানে gemini-pro দিন

# Telegram Bot Setup
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Gemini থেকে উত্তর নেয়া
        response = model.generate_content(message.text)
        # Telegram-এ রিপ্লাই দেওয়া
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "Dhor bot net thik kor")

print("বটটি এখন সক্রিয়...")
bot.polling()
