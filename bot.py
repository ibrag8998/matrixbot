from telebot import TeleBot

from os import environ

import funcs


def msg(b, m, text):
    b.send_message(m.chat.id, text)


bot = TeleBot(environ['TOKEN'])


@bot.message_handler(commands=['start'])
def started(message):
    msg(bot, message, 'Send me a matrix, so i will try to solve it. Example on how to send matrix:')
    msg(bot, message, '/mx\n1 2 3\n4 5 6\n7 8 9')


@bot.message_handler(commands=['mx'])
def notification(message):
    msg(bot, message, 'Now you can ignore the /mx command and just send me a matrix')


@bot.message_handler(content_types=['text'])
def solve(message):
    mx = []
    line = message.text.split('\n')
    row = len(line)
    if row == 0:
        return msg(bot, message, 'incorrect')
    for i in range(len(line)):
        if i == 0:
            continue
        else:
            mx.append(line[i].split(' '))
    col = len(mx[0])

    for r in range(row):
        for c in range(col):
            mx[r][c] = int(mx[r][c])

    if row == col:
        msg(bot, message, 'Determinant: ' + str(funcs.determinant(mx)))


if __name__ == '__main__':
    bot.polling()
