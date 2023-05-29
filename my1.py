import telebot
from telebot import types

 bot = telebot.TeleBot('5890895516:AAHfjmqu3sKP7cH0Y6JJTHPgyFSXQlYTADY')

# Приветственное сообщение , 11 кнопок+ кнопка обращение к оператору
@bot.massage_handler(commands=['start', 'main', 'hello'])
def start(massage):
        bot.send_message(massage.chat.id, '<p>Этот бот поможет вам разобраться с получением и закрытием актов и договоров, получением счетов и другими вопросами.</p>', parse_mode='html')

# Ответное сообщение по номеру кнопки или приветственное сообщение и кнопки.
@bot.massage_handler(commands=['1'])
def website (message):
    markup = types.InlineKeyboardButton("1.Как заключить Публичный договор для получения доступа к ИПС «СтройДОК онлайн»? ",
                                        text='Заключение Публичного договора возмездного предоставления доступа к информации от 29 апреля 2020 года производится путем присоединения Заказчика к Договору, '
                                             'т.е. посредством принятия (акцепта) условий Договора в целом.'
                                             'Фактом принятия (акцепта) условий Публичного договора является оформленный на нашем сайте оnline-заказ (https://stn.by/services/stroydoc/shop) '
                                             'и оплата заказанного пакета услуг в порядке и на условиях, определенных Публичным договором.',
                                        )


bot.polling(none_stop=True)



""" import telebot

bot = telebot.TeleBot('5890895516:AAHfjmqu3sKP7cH0Y6JJTHPgyFSXQlYTADY')
 
 @bot.message_handler(commands)