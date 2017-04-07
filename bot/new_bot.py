# 129944746
# 224746501
import telebot
import random
import config
import time
import math

bot = telebot.TeleBot(config.token)
op = False

while not op:
    op = False
    try:
        if tried:
            pass
        else:
            pass
    except:
        tried = False

    def message_history(message):
        date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(message.date))
        data = [date, message.from_user.first_name, message.from_user.last_name, "@" + message.from_user.username, message.chat.id,
                'text:' + message.text]
        data = str(data)
        data = data.replace("[", "").replace("]", "").replace("',", "").replace("'", "")
        with open('history.txt', 'a', encoding='utf8') as history:
            print(data, file=history)

    def mylog(message, text_of_bot_message):
        data = ['fromBot:', time.strftime("%a, %d %b %Y %H:%M:%S"), message.from_user.first_name, message.from_user.last_name,
                '@' + message.from_user.username, message.chat.id, 'text:' + text_of_bot_message]
        data = str(data)
        data = data.replace("[", "").replace("]", "").replace("',", "").replace("'", "")
        with open('history.txt', 'a', encoding='utf8') as history:
            print(data, file=history)

    @bot.message_handler(commands=["random"])
    def message_random(message):
        global op
        message_history(message)
        try:
            rndA = int(message.text.split()[1])
            rndB = int(message.text.split()[2])
            rndRes = random.randint(rndA, rndB)
            bot.send_message(message.chat.id, rndRes)
            mylog(message, rndRes)
        except:
            bot.send_message(message.chat.id, "Введите a и b после \nкомманды /random")
            mylog(message, "Введите a и b после \nкомманды /random")
        op = True


    @bot.message_handler(commands=["help"])
    def message_help(message):
        global op
        message_history(message)
        helptext = "Список команд:\n\n/help - список команд\n/random (a) (b) - произвольное число от a до b\n" \
                   "/send (id) - отправляет сообщение пользователю с данным ID"
        bot.send_message(message.chat.id, helptext)
        mylog(message, helptext)
        op = True


    @bot.message_handler(commands=["send"])
    def message_send(message):
        global op
        message_history(message)
        newA = message.text.split()
        try:
            ID = int(newA[1])
            try:
                mes = newA[2:]
                mesA = ""
                for i in mes:
                    mesA += " "
                    mesA += i
                bot.send_message(ID, mesA)
                mylog(message, mesA)
            except:
                bot.send_message(ID, "some message")
                mylog(message, "some message")
            bot.send_message(message.chat.id, "Успешно отправлено.")
            mylog(message, "Успешно отправлено.")
        except:
            bot.send_message(message.chat.id, "Введите ID после комманды /send")
            mylog(message, "Введите ID после комманды /send")
        op = True

    @bot.message_handler(commands=["creator", "admin"])
    def message_admin(message):
        global op
        message_history(message)
        adminID = 224746501
        try:
            admin_txt = message.from_user.first_name + " " + message.from_user.last_name + " вызывает тебя."
        except:
            admin_txt = "Аноним вызывает тебя."
        man_txt = "Админ тебе напишет."
        bot.send_message(adminID, admin_txt)
        print("fromBot:", time.strftime("%a, %d %b %Y %H:%M:%S"), "Oleg", "Okoyomov",
                "@" + "olegok2003", "224746501", admin_txt)
        bot.send_message(message.chat.id, man_txt)
        mylog(message, man_txt)
        op = True

    @bot.message_handler(commands=["quad"])
    def message_quad(message):
        global op
        message_history(message)
        ur = message.text
        A = ur[ur.index('/quad ')+6:ur.index('x2')]
        if A == "+":
            A = 1
        elif A == "-":
            A = -1
        else:
            A = int(A)
        ur = ur[ur.index('x2')+2:]
        B = ur[:ur.index('x')]
        if B == "+":
            B = 1
        elif B == "-":
            B = -1
        else:
            B = int(B)
        ur = ur[ur.index('x')+1:]
        C = ur[:ur.index('=')]
        if C == "+":
            C = 1
        elif C == "-":
            C = -1
        else:
            C = int(C)
        D = B**2 - 4*A*C
        if D < 0:
            bot_msg1 = 'Данное уравнение не имеет решений.'
        elif D == 0:
            x = (-B) / (2*A)
            bot_msg1 = 'Дискриминант = 0 \nx = ' + str(x)
        else:
            x1 = (-B + math.sqrt(D)) / (2*A)
            x2 = (-B - math.sqrt(D)) / (2*A)
            bot_msg1 = 'Дискриминант = ' + str(D) + '\nx1 = ' + str(x1) + '\nx2 = ' + str(x2)
        bot.send_message(message.chat.id, bot_msg1)
        mylog(message, bot_msg1)
        op = True
        """
        SUM = -B / A
        MUL = C / A
        l = -SUM - 1
        r = SUM
        if MUL == 0:
            x1 = 0
            x2 = SUM
            bot_msg2 = 'Сумма корней = ', str(SUM), '\nПроизведение корней = 0 \nx1 = ' + str(x1), '\nx2 = ' + str(x2)
        else:
            ops = 0
            while True:
                x1 = (r + l) / 2
                if x1 == 0:
                    x1 += 1
                X2 = MUL / x1
                x2 = SUM - x1
                if x2 > X2:
                    r = x1
                elif x2 < X2:
                    l = x1
                else:
                    bot_msg2 = 'Сумма корней = ', str(SUM), '\nПроизведение корней = ' + str(MUL) + '\nx1 = ' + \
                               str(x1), '\nx2 = ' + str(x2)
                    break
                if ops > 1000:
                    bot_msg2 = 'Сумма корней = ', str(SUM), '\nПроизведение корней = ' + str(MUL) + '\nx1 = ' + \
                               str(x1), '\nx2 = ' + str(x2)
                    break
                ops += 1
        bot.send_message(message.chat.id, bot_msg2)
        mylog(message, bot_msg2)
        """


    @bot.message_handler(content_types=["text"])
    def message_any(message):
        global tried, op
        message_history(message)
        text = message.text
        eng = "`qwertyuiop[]asdfghjkl;'\zxcvbnm,./"
        rus = "ёйцукенгшщзхъфывапролджэ\ячсмитьбю."
        ENG = '~QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?' + '!@#$%^&*()'
        RUS = "ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ," + '!"№;%:?*()'
        new_message = ""
        if not op and tried:
            bot.send_message(message.chat.id, "Я не понял вас.")
            mylog(message, "Я не понял вас.")
            op = True
        elif not op:
            for i in text:
                if i in eng:
                    new_message += rus[eng.index(i)]
                elif i in rus:
                    new_message += eng[rus.index(i)]
                elif i in ENG:
                    new_message += RUS[ENG.index(i)]
                elif i in RUS:
                    new_message += ENG[RUS.index(i)]
        bot.send_message(bot.get_me().id, new_message)
        tried = True

if __name__ == "__main__":
    bot.polling(none_stop=True)
