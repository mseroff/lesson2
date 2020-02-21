#Установите модуль ephem
#Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, например /planet Mars
#В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
#При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def planet_constellation(bot, update):
    u_m = update.message
    today_date = datetime.datetime.today().strftime("%Y/%m/%d")

    planet_dict = {
                    'Mars': ephem.Mars(today_date),
                    'Jupiter': ephem.Jupiter(today_date),
                    'Uranus': ephem.Uranus(today_date),
                    'Moon': ephem.Moon(today_date),
                    'Saturn': ephem.Saturn(today_date)
    }

    get_user_respond_list = u_m.text.split()

    if len(get_user_respond_list) > 1:
            planet_name = get_user_respond_list[1].capitalize()
            if planet_name in planet_dict:
                planet_coords = planet_dict[planet_name]
                constellation = ephem.constellation(planet_coords)
                user_text = "Hello {}! You are wrote planet: {}, constellation: {}".format(u_m.chat.first_name, planet_name, constellation)
                logging.info("User: %s, Chat id: %s, Message: %s", u_m.chat.username, u_m.chat.id, u_m.text)
                print(u_m)
                u_m.reply_text(user_text)
            else:
                u_m.reply_text('Planet {} is not found, please try again.'.format(planet_name))


def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)

    logging.info("Bot is starting...")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(CommandHandler('planet', planet_constellation))

    mybot.start_polling()
    mybot.idle()

main()
