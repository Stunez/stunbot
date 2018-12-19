{"ok":true,"result":[{
"update_id":999590778,
"message":{
"message_id":265,"from":{
"id":439943433,"is_bot":false,"first_name":"Unelos","username":"Unelos","language_code":"ru-RU"},
"chat":{"id":439943433,"first_name":"Unelos","username":"Unelos","type":"private"},
"date":1541898899,"text":"/start","entities":[s
{"offset":0,"length":6,"type":"bot_command"}
]
}
},
{"update_id":999590779,
"message":{
"message_id":266,
"from": {"id":439943433,"is_bot":false,"first_name":"Unelos","username":"Unelos","language_code":"ru-RU"}
,
"chat":{"id":439943433,"first_name":"Unelos","username":"Unelos","type":"private"},
"date":1541898919,
"location":{"latitude":43.257851,"longitude":76.887656}}
}
]
}

[{"id":"7","name_kaz":"ОҢТҮСТІК КОРЕЯ РЕСПУБЛИКАСЫНЫҢ ВОНАСЫ","edinica_izmerenia":"ТЕНГЕ","sootnowenie":"100","name_rus":"ВОНА РЕСПУБЛИКИ ЮЖНАЯ КОРЕЯ","kurs":"32.26","kod":"KRW"}
]












==========================
from telegram import update
from telegram import bot
from telegram.ext import Updater

token = '641542217:AAHj-pmdV9Gg9IZ6epNOQDUCiLokDhKZiWs'
updater = Updater(token)
bot = bot.Bot(token)

chat_id = update.Message.chat_id

#print(chat_id)
c = "@cookiesinthefloor"

#bot.polling(none_stop=True, interval=0)

bot.send_message(439943433,"Hello Worlo")

from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373000.0
latinput = float(input())
loninput = float(input())
location = {
"lat1" : 43.235051,
'lon1' : 76.909720, #центркредит сатпаева манаса
'lat2' : 43.235210,
'lon2' : 76.908025, #tamoto
'lat3' : 43.240199,
'lon3' : 76.905399, #Сбербанк, ТЦ Глобус
'lat4' : 43.240670,
'lon4' : 76.914141 #Народный банк, Urban Athletic
}

#задаем переменную для цикла
dlon = 0
dlat = 0
distance2 = 9999999999
distance = 0
latnum = 0
#------
#подсчет самого близкого отделения банка
for lat,lonnum in location.items():
	
	lonnum = float(lonnum)
	
	for i in lat:
		
		if i == 'o':
			dlon = radians(loninput) - radians(lonnum)
			dlat = radians(latinput)- radians(latnum)
			a = sin(dlat / 2)**2 + cos(latnum) * cos(latinput) * sin(dlon / 2)**2
			c = 2 * atan2(sqrt(a), sqrt(1 - a))	
			distance = R * c
		elif i == 'a': 
			latnum = lonnum
	if distance == 0:
		pass
	elif distance2 > distance:
		distance2 = distance
#------

print("Result:", int(distance2))


=================================
import requests
from time import sleep
url = "https://api.telegram.org/bot641542217:AAHj-pmdV9Gg9IZ6epNOQDUCiLokDhKZiWs/"




def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()
    
def last_update(data):  
	results = data['result']
	total_updates = len(results) - 1
	return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'ты предал каноху')
           update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()

def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()



============================
class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update



def main():  
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1
greet_bot = BotHandler(token)  
greetings = ('здравствуй', 'привет', 'ку', 'здорово')  
now = datetime.datetime.now()

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()

========================
import telebot
import config
import requests

bot_token = '641542217:AAHj-pmdV9Gg9IZ6epNOQDUCiLokDhKZiWs'
bot = telebot.TeleBot(token=bot_token)
import datetime

@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


# Инлайн-режим с непустым запросом
@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    # Добавляем колбэк-кнопку с содержимым "test"
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
    results = []
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)


# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")

if __name__ == '__main__':
    bot.polling(none_stop=True)
    ==========
    import telebot
import json

API_TOKEN = '761916527:AAHRNgBRIQMVKfeqGxmPF3xgxMeKqETeuOg'
bot = telebot.TeleBot(API_TOKEN)
latt = 0.0
lonn = 0.0
tt = ""

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def remove_char(str, n):
    first_part = str[:n]
    last_pasrt = str[n + 1:]
    return first_part + last_pasrt


@bot.message_handler(func=lambda message: True, content_types=['location'])
def handle_location(message):
    loc = "'location':"
    lon = ""
    lat = ""
    undiffer_char_lat = 1
    undiffer_char_lon = 1
    msg = str(message)
    msg2 = msg.split()

    for i in range(len(msg2)):
        if msg2[i] == loc:
            lon = msg2[i+2]
            lat = msg2[i+4]
            break

    for i in range(len(lon)):
        if not lat[i].isdigit():
            undiffer_char_lat += 1

    for i in range(len(lat)):
        if not lat[i].isdigit():
            undiffer_char_lon += 1

    latt = lat[:-3]
    lonn = lon[:-3]


bot.polling()
