from telebot import TeleBot

from os import environ

import funcs


def msg(b, m, text):
    b.send_message(m.chat.id, text)


bot = TeleBot(environ['TOKEN'])


@bot.message_handler(commands=['start'])
def started(message):
    msg(bot, message, 'Send me a matrix, so i will try to solve it.')


@bot.message_handler(commands=['mx'])
def solve(message):
    mx = []
    line = message.text.split('\n')
    row = len(line)-1
    if row == 0:
        return msg(bot, message, 'uncorrect')
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
