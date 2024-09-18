import telebot
from telebot import types
from worker import shutdown, reboot, sleep

bot = telebot.TeleBot('7267296954:AAELfW5r-fOMsviDxSBIiouB6qbcKmqV8Hw')

user_actions = {}

@bot.message_handler(commands=['start', 's'])
def main(ctx): 
    markup = types.ReplyKeyboardMarkup()
    pc_shutdown = types.KeyboardButton('🚫 Shutdown')
    pc_reboot = types.KeyboardButton('🔄 Reboot')
    pc_sleep = types.KeyboardButton('✨ Sleep')
    markup.row(pc_shutdown, pc_reboot, pc_sleep)
    bot.send_message(ctx.chat.id, f'💙 Hello, {ctx.from_user.username}', reply_markup=markup)
    bot.register_next_step_handler(ctx, on_click)

def check_pass(ctx):
    user_id = ctx.from_user.id
    bot.delete_message(ctx.chat.id, ctx.message_id)
    
    if ctx.text == '1902':
        bot.send_message(ctx.chat.id, '✅ Access granted')
        if user_id in user_actions:
            action = user_actions[user_id]
            perform_function(ctx, action)
            del user_actions[user_id]
    else:
        bot.send_message(ctx.chat.id, '❌ Access denied')
        bot.register_next_step_handler(ctx, check_pass)

def on_click(ctx):
    user_id = ctx.from_user.id
    user_actions[user_id] = ctx.text
    bot.send_message(ctx.chat.id, '🪪 Please write pass:')
    bot.register_next_step_handler(ctx, check_pass)

def perform_function(ctx, action):
    if action == '🚫 Shutdown':
        bot.send_message(ctx.chat.id, '⛔ System will shutdown...')
        shutdown()  # Вызываем функцию завершения работы
    elif action == '🔄 Reboot':
        bot.send_message(ctx.chat.id, 'System will reboot...')
        reboot()  # Вызываем функцию перезагрузки
    elif action == '✨ Sleep':
        bot.send_message(ctx.chat.id, '🧿 System will go to sleep...')
        sleep()  # Вызываем функцию перевода в спящий режим
    else:
        bot.send_message(ctx.chat.id, '🗿 Unknown action.')

    bot.register_next_step_handler(ctx, on_click)

bot.polling(non_stop=True)
