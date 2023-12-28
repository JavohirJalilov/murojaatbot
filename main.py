from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from handlers import start, send_message_channel

def main(dispatcher):
    dispatcher.add_handler(CommandHandler('start',start))
    # updater.dispatcher.add_handler(CommandHandler('student_users',student_users))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document,arxiv))
    dispatcher.add_handler(MessageHandler(Filters.text,send_message_channel))
    return dispatcher
