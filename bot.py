from telebot import TeleBot
import pickle
import traceback


TOKEN = 'Your token'
bot = TeleBot(token = TOKEN)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Welcome to the Comment Classification Bot!\n\n"
        "📝 Just send me any message in English, and I’ll tell you if it’s Positive, Negative, or Neutral.\n\n"
        "Let’s gooo 🚀"
    )

@bot.message_handler(func=lambda msg: True)
def analyze(message):
    user_text = message.text
    try:
        prediction = model.predict([user_text])[0]
        if prediction == 1:
            label = "Positive 😊"
        elif prediction == 0:
            label = "Neutral 😐"
        else:
            label = "Negative 😞"
        bot.send_message(message.chat.id, f"Your comment: {label}")
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Could not analyze the comment.")
        print("Error:", e)

bot.polling()