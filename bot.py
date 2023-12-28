from telegram.ext import Updater
from main import main

TOKEN = '6495035328:AAHRU83uolqEybVkjY5XInawUjakQqJX8nc'
updater = Updater(token=TOKEN)

# dispatcher
dispatcher = updater.dispatcher

# adding handlers
dispatcher = main(dispatcher)

# Start the Bot
updater.start_polling()

updater.idle()