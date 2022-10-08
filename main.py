import requests
import json
from telebot import TeleBot
from config import telegram_token

bot = TeleBot(token=telegram_token)

@bot.message_handler(content_types=['text'])
def crypto_price(message):
    coin = message.text.lower()
    
    try:
        api = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response_api = requests.get(api)
        data = response_api.text
        data = json.loads(data)
        #print(data[coin]['usd'])
        bot.send_message(chat_id=message.chat.id, text=f"Current price of {message.text} is ${data[coin]['usd']}")
    except:
        bot.send_message(chat_id=message.chat.id, text="Coin wasn't found")


if __name__ == "__main__":   
    bot.polling()






