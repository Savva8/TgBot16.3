import telebot
from telebot import types

bot = telebot.TeleBot('5652813300:AAE68arICrOjeYBn2b1l_NBjGB22d8jGAKQ')

concrete = 0
sand = 0
brick = 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    func = types.InlineKeyboardButton("Функции")
    markup.add(func)
    if message.from_user.last_name:
        bot.send_message(message.chat.id, f'Здравствуйте, \
{message.from_user.first_name} {message.from_user.last_name}, для ведения '
                                          f'учета нажмите кнопку Функции',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Здравствуйте, \
{message.from_user.first_name}, для ведения учета нажмите кнопку Функции',
                         reply_markup=markup)


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Вывести текущее количество расходников':
        bot.send_message(message.chat.id, f"Остаток цемента: {concrete} кг \n"
                                          f"Остаток песка: {sand} кг \n"
                                          f"Остаток кирпичей: {brick} шт")
    elif message.text == 'Изменить количество расходников':
        change(message)
    elif message.text == 'Функции' or message.text == '/functions' or \
            message.text == 'Назад':
        functions(message)
    elif message.text == 'Цемент':
        concrete_fun(message)
    elif message.text == 'Песок':
        sand_fun(message)
    elif message.text == 'Кирпичи':
        brick_fun(message)
    else:
        bot.send_message(message.chat.id, 'Неверный ввод, нажмите /functions')


@bot.message_handler(commands=['functions'])
def functions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    current_but = types.InlineKeyboardButton("Вывести текущее количество "
                                             "расходников")
    change_but = types.InlineKeyboardButton("Изменить количество расходников")
    markup.add(current_but, change_but)
    bot.send_message(message.chat.id,
                     'Для учета расходников нажмите одну из кнопок',
                     reply_markup=markup)


@bot.message_handler(commands=['change'])
def change(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    concrete_but = types.InlineKeyboardButton("Цемент")
    sand_but = types.InlineKeyboardButton("Песок")
    brick_but = types.InlineKeyboardButton("Кирпичи")
    func = types.InlineKeyboardButton("Назад")
    markup.add(concrete_but, sand_but, brick_but, func)
    bot.send_message(message.chat.id,
                     'Выберите кнопку с названием расходника, количество'
                     ' которого необходимо изменить',
                     reply_markup=markup)


@bot.message_handler(commands=['concrete_fun'])
def concrete_fun(message):
    bot.send_message(message.chat.id, 'Введите на сколько кг изменилось '
                                      'количество цемента '
                                      '(например: +20 / -2.5)')

    @bot.message_handler(func=lambda message: message.text is not None and
                         message.chat.type == 'private')
    def check_concrete(message):
        global concrete
        try:
            num = float(message.text)
            if (concrete + num) < 0:
                bot.send_message(message.chat.id,
                                 'Ошибка: Результат вычислений будет '
                                 'отрицательным, для продолжения выберите '
                                 'одну из кнопок')
            else:
                concrete += num
                bot.send_message(message.chat.id, f"Остаток цемента: "
                                                  f"{concrete} кг, для "
                                                  f"продолжения выберите "
                                                  f"одну из кнопок")
        except ValueError:
            bot.send_message(message.chat.id,
                             'Ошибка: Некорректный формат ввода, '
                             'для продолжения выберите одну из кнопок')

    bot.register_next_step_handler(message, check_concrete)


@bot.message_handler(commands=['sand_fun'])
def sand_fun(message):
    bot.send_message(message.chat.id, 'Введите на сколько кг изменилось '
                                      'количество песка '
                                      '(например: +20 / -2.5)')

    @bot.message_handler(func=lambda message: message.text is not None and
                         message.chat.type == 'private')
    def check_sand(message):
        global sand
        try:
            num = float(message.text)
            if (sand + num) < 0:
                bot.send_message(message.chat.id,
                                 'Ошибка: Результат вычислений будет '
                                 'отрицательным, для продолжения выберите '
                                 'одну из кнопок')
            else:
                sand += num
                bot.send_message(message.chat.id, f"Остаток песка: "
                                                  f"{sand} кг, для "
                                                  f"продолжения выберите "
                                                  f"одну из кнопок")
        except ValueError:
            bot.send_message(message.chat.id,
                             'Ошибка: Некорректный формат ввода, '
                             'для продолжения выберите одну из кнопок')

    bot.register_next_step_handler(message, check_sand)


@bot.message_handler(commands=['brick_fun'])
def brick_fun(message):
    bot.send_message(message.chat.id, 'Введите на сколько шт изменилось '
                                      'количество кирпичей '
                                      '(например: +20 / -2)')

    @bot.message_handler(func=lambda message: message.text is not None and
                         message.chat.type == 'private')
    def check_brick(message):
        global brick
        try:
            num = int(message.text)
            if (brick + num) < 0:
                bot.send_message(message.chat.id,
                                 'Ошибка: Результат вычислений будет '
                                 'отрицательным, для продолжения выберите '
                                 'одну из кнопок')
            else:
                brick += num
                bot.send_message(message.chat.id, f"Остаток кирпичей: "
                                                  f"{brick} шт, для "
                                                  f"продолжения выберите "
                                                  f"одну из кнопок")
        except ValueError:
            bot.send_message(message.chat.id,
                             'Ошибка: Некорректный формат ввода, '
                             'для продолжения выберите одну из кнопок')
    bot.register_next_step_handler(message, check_brick)


bot.polling(none_stop=True)
