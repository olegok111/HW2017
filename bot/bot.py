#129944746
#224746501
import telebot
import random
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['random'])
def message_random(message):
    try:
        rndA = int(message.text.split()[1])
        rndB = int(message.text.split()[2])
        rndRes = random.randint(rndA, rndB)
        bot.send_message(message.chat.id, rndRes)
    except:
        bot.send_message(message.chat.id, 'Введите a и b после \nкомманды /random')

@bot.message_handler(commands=['help'])
def message_help(message):
    bot.send_message(message.chat.id, 'Список команд:\n\n/help - список команд\n/random (a) (b) - произвольное число от a до b\n/send (id) - отправляет сообщение пользователю с данным ID')

@bot.message_handler(commands=['send'])
def message_send(message):
    newA = message.text.split()
    try:
        ID = int(newA[1])
        try:
            mes = newA[2:]
            mesA = ''
            for i in mes:
                mesA += ' '
                mesA += i
            bot.send_message(ID, mesA)
        except:
            bot.send_message(ID, 'some message')
        bot.send_message(message.chat.id, 'Успешно отправлено.')
    except:
        bot.send_message(message.chat.id, 'Введите ID после комманды /send')

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
        except:
            pass
@bot.message_handler(commands=['creator', 'admin'])
def message_admin(message):
    adminID = 224746501
    try:
        admin_txt = message.from_user.first_name + ' ' + message.from_user.last_name + ' вызывает тебя.'
    except:
        admin_txt = 'Аноним вызывает тебя.'
    man_txt = 'Админ тебе напишет.'
    bot.send_message(adminID, admin_txt)
    bot.send_message(message.chat.id, man_txt)
    

if __name__ == '__main__':
    bot.polling(none_stop=True)
