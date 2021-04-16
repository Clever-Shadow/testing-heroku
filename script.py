import re
import requests
import telebot
import config
import time
import hashlib
from os import environ
from flask import Flask
from bs4 import BeautifulSoup as BS
from collections import deque

bot=telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])
def main(message):
   bot.send_message(message.chat.id, "Ку")
    
if __name__=='__main__':
    bot.polling(none_stop=True, interval=0)