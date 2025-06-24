import os
import telebot
from telebot import types

TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_API_TOKEN_HERE")

bot = telebot.TeleBot(TOKEN)

CATEGORY_KEYBOARD = ['Бюджетный', 'Средний', 'Топовый']

CONFIGS = {
    'Бюджетный': (
        "Бюджетная сборка:\n"
        "- CPU: AMD Ryzen 5\n"
        "- GPU: NVIDIA GTX 1660\n"
        "- RAM: 16GB"
    ),
    'Средний': (
        "Средняя сборка:\n"
        "- CPU: AMD Ryzen 7\n"
        "- GPU: NVIDIA RTX 3060\n"
        "- RAM: 32GB"
    ),
    'Топовый': (
        "Топовая сборка:\n"
        "- CPU: Intel Core i9\n"
        "- GPU: NVIDIA RTX 4090\n"
        "- RAM: 64GB"
    ),
}

@bot.message_handler(commands=['start'])
def handle_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for cat in CATEGORY_KEYBOARD:
        markup.add(cat)
    bot.send_message(
        message.chat.id,
        "Привет! Выберите категорию игрового ПК:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda m: m.text in CATEGORY_KEYBOARD)
def handle_selection(message: types.Message):
    config = CONFIGS.get(message.text, "Конфигурация не найдена")
    bot.send_message(message.chat.id, config)

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
