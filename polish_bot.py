import telebot
import pyads
plc=pyads.Connection('10.177.3.80.1.1',851)
plc.open()
status=plc.read_by_name('GVL.REWIND_STATUS_H',pyads.PLCTYPE_INT)
length=plc.read_by_name('GVL.Lenght_Curr_Bot',pyads.PLCTYPE_REAL)
a='Длина ' +str(length);
bot=telebot.TeleBot('5147228460:AAEq1zua8ShVmgBqRQAZ5Ohftz-ScN79N5o')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        if message.text == "Статус":
                if status==4:
                        bot.send_message(message.chat.id, "Процесс запущен")
                else:
                        bot.send_message(message.chat.id, "Процесс остановлен")
        if message.text == "Длина ленты":
                bot.send_message(message.chat.id, text=a )
plc.close()
bot.polling(none_stop=True)                
