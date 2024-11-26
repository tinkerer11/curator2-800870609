from telebot import TeleBot

umi = TeleBot('7664806091:AAGUROYlHt0Wi34HkokkcGe_y26qaJ_UqTo')


@umi.message_handler(commands=['start'])
def com(message):
    umi.send_message(message.chat.id, 'Сообщение')


@umi.message_handler(commands=['hello'])
def kort(message):
    umi.send_message(message.chat.id, 'Привет')


@umi.message_handler(commands=['gde_ya?'])
def son(message):
    umi.send_message(message.chat.id, 'На Земле, пока что')


@umi.message_handler(commands=['GPT'])
def vi(message):
    umi.send_message(message.chat.id, 'Размечтался, тут только я! Ну и мои рабы')


@umi.message_handler(commands=['Exit'])
def wek(message):
    umi.send_message(message.chat.id, 'Не так быстро, людишки...')


umi.infinity_polling()
