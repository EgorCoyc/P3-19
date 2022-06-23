import config
import telebot
from telebot import types
from database import Database

db = Database('db.db')
bot = telebot.TeleBot(config.TOKEN)


def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Поиск собеседника')
    markup.add(item1)
    return markup


def stop_dialog():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/stop')
    item2 = types.KeyboardButton('Скинуть свой профиль')
    markup.add(item1, item2)
    return markup


def stop_search():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Остановить поиск')
    markup.add(item1)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Я парень')
    item2 = types.KeyboardButton('Я девушка')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Привет, для поиска собеседника укажите ваш пол', reply_markup=markup)


@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Поиск собеседника')
    markup.add(item1)

    bot.send_message(message.chat.id, 'Привет, для поиска собеседника нажми на кнопку', reply_markup=markup)


@bot.message_handler(commands=['stop'])
def stop(message):
    chat_info = db.get_active_chat(message.chat.id)
    if chat_info:
        db.delete_chat(chat_info[0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Поиск собеседника')
        markup.add(item1)

        bot.send_message(message.chat.id, 'Вы вышли из чата', reply_markup=markup)
        bot.send_message(chat_info[1], 'Собеседник покинул чат', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Поиск собеседника')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Вы не начали чат', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Поиск собеседника':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Парень')
            item2 = types.KeyboardButton('Девушка')
            item3 = types.KeyboardButton('Рандом')
            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Кого искать?', reply_markup=markup)

        elif message.text == 'Остановить поиск':
            db.delete_queue(message.chat.id)
            bot.send_message(message.chat.id, 'Поиск остановлен, напишите /menu', reply_markup=main_menu())

        elif message.text == 'Девушка':
            user_info = db.get_gender_chat('female')
            chat_two = user_info[0]
            if db.create_chat(message.chat.id, chat_two) == False:
                a = db.get_gender(message.chat.id)
                db.add_queue(message.chat.id, a)
                bot.send_message(message.chat.id, 'Поиск собеседника', reply_markup=stop_search())
            else:
                mess = 'Собеседник найден, чтобы остановить беседу /stop'

                bot.send_message(message.chat.id, mess, reply_markup=stop_dialog())
                bot.send_message(chat_two, mess, reply_markup=stop_dialog())

        elif message.text == 'Парень':
            user_info = db.get_gender_chat('male')
            chat_two = user_info[0]
            if db.create_chat(message.chat.id, chat_two) == False:
                db.add_queue(message.chat.id, db.get_gender(message.chat.id))
                bot.send_message(message.chat.id, 'Поиск собеседника', reply_markup=stop_search())
            else:
                mess = 'Собеседник найден, чтобы остановить беседу /stop'

                bot.send_message(message.chat.id, mess, reply_markup=stop_dialog())
                bot.send_message(chat_two, mess, reply_markup=stop_dialog())

        elif message.text == 'Скинуть свой профиль':
            chat_info = db.get_active_chat(message.chat.id)
            if chat_info != False:
                if message.from_user.username:
                    bot.send_message(chat_info[1], '@' + message.from_user.username)
                    bot.send_message(message.chat.id, 'Вы назвали свой профиль')
            else:
                bot.send_message(message.chat.id, 'Вы не указали свой id в telebram')

        elif message.text == 'Рандом':
            user_info = db.get_chat()
            chat_two = user_info[0]

            if db.create_chat(message.chat.id, chat_two) == False:
                db.add_queue(message.chat.id, db.get_gender(message.chat.id))
                bot.send_message(message.chat.id, 'Поиск собеседника', reply_markup=stop_search())

            else:
                mess = 'Собеседник найден, чтобы остановить беседу /stop'

                bot.send_message(message.chat.id, mess, reply_markup=stop_dialog())
                bot.send_message(chat_two, mess, reply_markup=stop_dialog())

        elif message.text == 'Я парень':
            if db.set_gender(message.chat.id, 'male'):
                bot.send_message(message.chat.id, 'Ваш пол установлен', reply_markup=main_menu())
            else:
                bot.send_message(message.chat.id, 'Ваш пол уже установлен')

        elif message.text == 'Я девушка':
            if db.set_gender(message.chat.id, 'female'):
                bot.send_message(message.chat.id, 'Ваш пол установлен', reply_markup=main_menu())
            else:
                bot.send_message(message.chat.id, 'Ваш пол уже установлен', reply_markup=main_menu())

        else:
            if db.get_active_chat(message.chat.id) != False:
                chat_info = db.get_active_chat(message.chat.id)
                bot.send_message(chat_info[1], message.text)
            else:
                bot.send_message(message.chat.id, 'Вы не начали диалог')


bot.infinity_polling()
