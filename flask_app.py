import telegram
from flask import Flask
from flask import request
from telegram.ext import Dispatcher

TOKEN = '6495035328:AAHRU83uolqEybVkjY5XInawUjakQqJX8nc'
bot = telegram.Bot(TOKEN)

app = Flask(__name__)

@app.route('/getInfo')
def getInfo():

    info = bot.get_webhook_info()
    return info.to_json()

@app.route('/set')
def setWebhook():
    
    HOOK_URL = 'https://metodistgamurojaat.pythonanywhere.com/'
    hook_bool = bot.setWebhook(url=HOOK_URL)
    return str(hook_bool)



@app.route('/', methods=['POST'])
def main():
    from main import main

    dp = Dispatcher(bot, None, workers=1)

    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        dp = main(dp)

        dp.process_update(update)


    return 'OK'