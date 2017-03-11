#129944746
#224746501
import config
import telebot
import random

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['random'])
def message_random(message):
    rndA = int(message.text.split()[1])
    rndB = int(message.text.split()[2])
    rndRes = random.randint(rndA, rndB)
    bot.send_message(message.chat.id, rndRes)

@bot.message_handler(commands=['help'])
def message_help(message):
    bot.send_message(message.chat.id, 'Список команд:\n\n/help - список команд\n/random (a) (b) - произвольное число от a до b\n/send (id) - отправляет сообщение пользователю с данным ID')

@bot.message_handler(commands=['send'])
def message_help(message):
    newA = message.text.split()
    ID = int(newA[1])
    bot.send_message(ID, 'some message')
    bot.send_message(message.chat.id, 'Успешно отправлено.')

@bot.message_handler(commands=['count'])
def message_calc(message):
    vyr = message.text.split()[1]
    if vyr[0].isdigit() == True:
        pl, mi, um, de = None, None, None, None
        try:
            pl = vyr.index('+')
            mi = vyr.index('-')
            um = vyr.index('*')
            de = vyr.index('/')

if __name__ == '__main__':
    bot.polling(none_stop=True)