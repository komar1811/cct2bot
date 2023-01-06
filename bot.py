import telebot

from constants import *
from helpers import get_kicked

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start', "help"])
def send_info(message):
    bot.send_message(message.chat.id,
                     '''Всем Привет, Я Чат Бот ССТ 2.0 \nИспользуй:
    \\team - чтобы узнать состав команд на ССТ 2.0
    \\stats - узнать количество сыгранных серий и баллов конкретного игрока
    \\team_stats - узнать количество баллов команды''')


@bot.message_handler(commands=['team'])
def send_team(message):
    try:
        name = message.text.split(" ")[1]
        team_members_unformatted = sh_kom.get_worksheet(0).get(TEAMS[name][1])[0]
        team_members = []
        for nickname in range(len(team_members_unformatted)):
            if team_members_unformatted[nickname] in get_kicked():
                team_members.append(team_members_unformatted[nickname] + " (кикнут)")
            else:
                team_members.append(team_members_unformatted[nickname])
        bot.send_message(message.chat.id, f"Команда {TEAMS[name][0]}: \n" + "\n".join(team_members))
    except KeyError:
        bot.send_message(message.chat.id, "Неправильный ник")


@bot.message_handler(commands=['team_stats'])
def send_team_stats(message):
    try:
        name = message.text.split(" ")[1]
        team_stat = sh_kam.get_worksheet(2).get(TEAMS[name][2])[0][0]
        bot.send_message(message.chat.id, f"Команда {TEAMS[name][0]}\nСумма баллов: {team_stat}")
    except KeyError:
        bot.send_message(message.chat.id, "Неправильный ник")


@bot.message_handler(commands=['stats'])
def send_stats(message):
    try:
        name = message.text.split(" ")[1]
        player_stat_unformatted = sh_kam.get_worksheet(2).get(PLAYERS[name][0])[0]
        if message.text.split(" ")[1] in get_kicked():
            name += " (кикнут)"
        series_stats = ""
        for counter in range(len(player_stat_unformatted) - 2):
            series_stats += f"{series[counter]} серия: {player_stat_unformatted[counter + 2]}\n"
        bot.send_message(message.chat.id,
                         f'''{name} ({PLAYERS[message.text.split(' ')[1]][2]})
        Сумма баллов: {player_stat_unformatted[1]} 
        Сыграно серий: {len(player_stat_unformatted) - 2}
        {series_stats}''')
    except KeyError:
        bot.send_message(message.chat.id, "Неправильный ник")


if __name__ == '__main__':
    bot.polling(none_stop=True)
