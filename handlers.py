
from telegram import ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton
from telegram import Update
from telegram.ext import CallbackContext
import telegram
import os

def start(update,context):
    first_name = update.message.from_user.first_name

    # reply_markup = ReplyKeyboardMarkup([[contact]],resize_keyboard=True)
    text = f"Assalomu aleykum {first_name}❕\n\nSamarqand viloyati Pedagoglarni yangi metodikalarga o'rgatish milliy markazi Informatika fani metodisti Xushvaqtov Akmaljon Kalandarovichga ta'lim bo'yicha taklif va murojaatlaringizni yo'llang!\n\nQayta a'loqaga chiqish uchun raqamingizni ham qoldiring!"
    update.message.reply_text(text=text)

def send_message_channel(update:Update,context:CallbackContext):
    # phone_number = update.message.contact.phone_number
    text = update.message.text
    chat_id = update.message.chat.id

    first_name = update.message.from_user.first_name
    user_name = update.message.from_user.username

    from_message = f"Yuboruvchi nomi: {first_name}\n"
    if user_name != None:
        from_message += f"Telegram username: @{user_name}"

    from_message += f"\n\nMUROJAAT MATNI:\n {text}"

    bot = context.bot
    chanel_id = -1001924177502
    bot.sendMessage(chanel_id, from_message)
    bot.sendMessage(chat_id, "Murojaatingiz muvaffaqiyatli yuborildi!")

