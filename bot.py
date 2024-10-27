import requests
import telebot
import random
from bot_logic import gen_emodji
from config import token

import os
print(os.listdir('images'))

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот с абсолютно случайными возможностями!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['mems'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
        '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)

def get_dog_image_url():    
        url = 'https://random.dog/woof.json'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
@bot.message_handler(commands=['dog'])
def dog(message):
        '''По команде dog вызывает функцию get_dog_image_url и отправляет URL изображения собачки'''
        image_url = get_dog_image_url()
        bot.reply_to(message, image_url)

def get_fox_image_url():    
        url = 'https://randomfox.ca/floof/'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
@bot.message_handler(commands=['fox'])
def fox(message):
        '''По команде fox вызывает функцию get_fox_image_url и отправляет URL изображения лисы'''
        image_url = get_fox_image_url()
        bot.reply_to(message, image_url)

def get_pokemon_image_url():    
        url = 'https://pokeapi.co'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
@bot.message_handler(commands=['pokemon'])
def pokemon(message):
        '''По команде duck вызывает функцию get_pokemon_image_url и отправляет URL изображения покемона'''
        image_url = get_pokemon_image_url()
        bot.reply_to(message, image_url)

@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

bot.infinity_polling(allowed_updates=telebot.util.update_types)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()
