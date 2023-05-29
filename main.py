#import webbrowser
import telebot
from telebot import types

# Считываю свой токен
mytoken = ('5890895516:AAHfjmqu3sKP7cH0Y6JJTHPgyFSXQlYTADY')
bot = telebot.TeleBot(mytoken)

BACK = 'Назад'

# Варианты ответов пользователю, если тот ввел непонятное боту сообщение
answers = ['Извините, я вас не понимаю. Вот контакты оператора @VSEMVEBINAR']

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('1')
    button2 = types.KeyboardButton('2')
    button3 = types.KeyboardButton('3')
    button4 = types.KeyboardButton('4')
    button5 = types.KeyboardButton('5')
    button6 = types.KeyboardButton('6')
    button7 = types.KeyboardButton('7')
    button8 = types.KeyboardButton('8')
    button9 = types.KeyboardButton('9')
    button10 = types.KeyboardButton('10')
    button11 = types.KeyboardButton('11')
    button12 = types.KeyboardButton('12')
    markup.row(button1,button2,button3)
    markup.row(button4, button5, button6)
    markup.row(button7, button8, button9)
    markup.row(button10, button11, button12)





    if message.text == '/start':
        # Отправляю приветственный текст
        bot.send_message(
            message.chat.id,
            f'''
Здравствуйте, {message.from_user.first_name}!
Добрый день. Этот бот поможет вам разобраться с получением и закрытием актов, заключением договоров, заказом доступа к ИПС, получением счетов, получить логин и пароль. Поможет авторизоваться, узнать есть ли у вас доступ к ИПС, и другие вопросы.
1. Как заключить Публичный договор для получения доступа к ИПС «СтройДОК онлайн»? 
2. Как заказать доступ к ИПС «СтройДОК онлайн»?
3. Как получить счет для оплаты услуги по предоставлению доступа к ИПС «СтройДОК онлайн»?
4. Я оплатил(а) доступ к ИПС «СтройДОК онлайн», но не получил(а) логины и пароли.
5. Я не получил(а) акт оказанных услуг предоставления доступа к ИПС «СтройДОК онлайн».
6. Не могу авторизоваться для доступа к ИПС «СтройДОК онлайн» по полученным логинам/паролям.
7. Как узнать, есть ли у нас действующий доступ к ИПС «СтройДОК онлайн»?
8. Являются ли документы, распечатанные из ИПС «СтройДОК онлайн» официальными изданиями?
9. Как приобрести ТНПА на бумажном носителе?
10. Как проактуализировать ТНПА и документы?
11. Могу ли я актуализировать фонд ТНПА на бумажном носителе, распечатав изменения из ИПС «СтройДОК онлайн»?
12. Здесь нет необходимого мне вопроса, обратиться к оператору @VSEMVEBINAR
            ''',
            reply_markup=markup
        )
    else:
        bot.send_message(message.chat.id,'Добро пожаловать в главное меню!',reply_markup=markup)

# Обработка фото. Если пользователь пришлет фото, то бот отреагирует на него.
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')

# Обработка обычных текстовых команд, описанных в кнопках
@bot.message_handler()
def info(message):
    if message.text == '1':
         Chapter1(message)
    elif message.text == '2':
        Chapter2(message)
    elif message.text == '3':
        Chapter3(message)
    elif message.text == '4':
        Chapter4(message)
    elif message.text == '5':
        Chapter5(message)
    elif message.text == '6':
        Chapter6(message)
    elif message.text == '7':
        Chapter7(message)
    elif message.text == '8':
        Chapter8(message)
    elif message.text == '9':
        Chapter9(message)
    elif message.text == '10':
        Chapter10(message)
    elif message.text == '11':
        Chapter11(message)
    elif message.text == '12':
        Chapter12(message)
    elif message.text == BACK:
        welcome(message)
    # Если пользователь написал свое сообщение, то бот отвечает answers !!!!!!!!????????
    else:
        bot.send_message(message.chat.id, answers)

# Функция, отвечающая за 1 вопрос
@bot.message_handler(['1'])
def Chapter1(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     button1 = types.KeyboardButton(BACK)
     bot.send_message(message.chat.id, 'Заключение Публичного договора возмездного предоставления доступа к информации от 29 апреля 2020 года производится путем присоединения Заказчика к Договору, т.е. посредством принятия (акцепта) условий Договора в целом. Фактом принятия (акцепта) условий Публичного договора является оформленный на нашем сайте оnline-заказ (https://stn.by/services/stroydoc/shop) и оплата заказанного пакета услуг в порядке и на условиях, определенных Публичным договором.', reply_markup=markup)
     markup.row(button1)

# Функция, отвечающая за 2 вопрос
def Chapter2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Для получения доступа к ИПС «СтройДОК онлайн» необходимо ознакомиться с условиями Публичного договора возмездного предоставления доступа к информации от 29 апреля 2020 года и оформить online-заказ на нашем сайте https://stn.by/info/stroydoc_online/shop
После получения Вашей заявки на Ваш e-mail будет направлен счет для оплаты.
''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 3 вопрос
def Chapter3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Для получения счета на оплату услуги по предоставлению доступа к ИПС «СтройДОК онлайн» необходимо ознакомиться с условиями Публичного договора возмездного предоставления доступа к информации от 29 апреля 2020 года и оформить online-заказ на нашем сайте https://stn.by/info/stroydoc_online/shop
В течение 5 (пяти) рабочих дней счет для оплаты будет направлен на указанным Вами  e-mail.
''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 4 вопрос
def Chapter4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Персональные идентификационные данные (логин(ы) и пароль(и)) передаются Заказчику посредством электронного письма после обязательного заполнения Заказчиком информации об ответственном в электронной форме по ссылке, направленной в письме со счетом на оплату. ''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 5 вопрос
def Chapter5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''В соответствии с условиями Публичного договора возмездного предоставления доступа к информации от 29 апреля 2020 года (пункт 6) акт сдачи-приемки оказанных услуг составляется Исполнителем и Заказчиком единолично в день активации доступа к ТНПА и документам через Систему и признается Сторонами первичным учетным документом. 
Номер акту сдачи-приемки оказанных услуг присваивается Сторонами аналогичный номеру счета на оплату.
Примерная форма акта сдачи-приемки оказанных услуг размещена на нашем сайте https://stn.by/files/act_online.pdf?v=20220215 
 ''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 6 вопрос
def Chapter6(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, 'В случае, если Вам не удается авторизоваться на портале normy.by для работы с ИПС «СтройДОК онлайн» необходимо: !\n- убедиться, что Ваша организация имеет оплаченный доступ к ИПС «СтройДОК онлайн» (портал normy.by, раздел «ПОЛЬЗОВАТЕЛИ ИПС»); !\n- убедиться, что отсутствие доступа к ТНПА и документам через Систему не связано с: аварийными ситуациями; заменой оборудования, программного обеспечения и/или проведением других ремонтных работ в Вашей организации; неполадками в работе компьютерного, телекоммуникационного оборудования или каналов связи (в том числе оборудования оператора, предоставляющего Вам услуги связи); перебоями в работе компьютерной сети Интернет и недостаточном качестве или скорости соединения при выходе в сеть Интернет по вине провайдеров телекоммуникационных услуг и/или поставщиков используемого программного обеспечения. !\nПри отсутствии вышеперечисленных причин необходимо обратиться в отдел информационно!\n-коммуникационных технологий по телефонам: (017) 373-69-08, (044) 537-41-03, (044) 537-41-04; e-mail: stroydoc@stn.by. ', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 7 вопрос
def Chapter7(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id,'Информацию о заключенных договорах с резидентами Республики Беларусь по предоставлению доступа к ИПС «СтройДОК онлайн» можно получить без авторизации на портале normy.by в разделе «ПОЛЬЗОВАТЕЛИ ИПС». ' , reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 8 вопрос
def Chapter8(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, 'Официальными электронными изданиями признаются документы, находящиеся в составе ИПС «СтройДОК онлайн». Документ, распечатанный из ИПС «СтройДОК онлайн», является копией официального электронного издания и может использоваться исключительно в ознакомительных целях. РУП «СТРОЙТЕХНОРМ» не несет ответственность за актуальность текстов документов, распечатанных из ИПС «СтройДОК онлайн».  ', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 9 вопрос
def Chapter9(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Для приобретение документов на бумажном носителе необходимо ознакомиться с условиями Публичного договора и оформить online-заказ на нашем сайте https://stn.by/info/typo 
После получения Вашей заявки на Ваш e-mail будет направлен счет для оплаты.
''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 10 вопрос
def Chapter10(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, '''Можно также воспользоваться услугами по актуализации ТНПА и документов, которые оказывает РУП «СТРОЙТЕХНОРМ» на основании присоединения к Публичному договору (https://stn.by/info/typo ):
пакет «СтройИнфо»;
пакет «Разовая актуализация фонда»;
пакет «Годовая актуализация фонда»;
«Организация ведения фонда ТНПА».
 ''', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 11 вопрос
def Chapter11(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, 'Актуализация фонда ТНПА в организации осуществляется в соответствии с выбранным источником комплектования фонда. Не допускается актуализация официальных печатных изданий ТНПА посредством приобретения доступа к ИПС «СтройДОК онлайн» и в обратном порядке. ', reply_markup=markup)
    markup.row(button1)

# Функция, отвечающая за 12 вопрос
def Chapter12(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(BACK)
    bot.send_message(message.chat.id, 'Здесь нет необходимого мне вопроса, обратиться к оператору @VSEMVEBINAR ', reply_markup=markup)
    markup.row(button1)



if __name__ == '__main__':

    # Строчка, чтобы программа не останавливалась
    bot.polling(none_stop=True)