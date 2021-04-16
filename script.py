import telebot
import config

bot=telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])
def main(message):
   bot.send_message(message.chat.id, "Ку")
    
if __name__=='__main__':
    bot.polling(none_stop=True, interval=0)