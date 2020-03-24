from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging, requests, json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

LOLKEY=''

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    keyboard=[[InlineKeyboardButton("EUW", callback_data='euw1'), 
        InlineKeyboardButton("RU", callback_data='ru'),
        InlineKeyboardButton("EUN", callback_data='eun1')],
        [InlineKeyboardButton("BR", callback_data='br1'),
        InlineKeyboardButton("JP", callback_data='jp1'),
        InlineKeyboardButton("KR", callback_data='kr')],
        [InlineKeyboardButton("LA1", callback_data='la1'),
        InlineKeyboardButton("LA2", callback_data='la2'),
        InlineKeyboardButton("NA", callback_data='na1')],
        [InlineKeyboardButton("OC", callback_data='oc1'),
        InlineKeyboardButton("TR", callback_data='tr1')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    #context.bot.send_message(chat_id=update.effective_chat.id, text="Type /help for commands. Please choose your region: ", reply_markup=reply_markup)
    update.message.reply_text('Type /help for commands. Please choose your region: ', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    region=query.data
    context.user_data['region']=query.data
    query.edit_message_text(text="Selected option: {}".format(query.data) + ". Write your Username: ")

def rank(update, context):
    us = " ".join(context.args)
    response=requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def rankru(update, context):
    us = " ".join(context.args)
    response=requests.get('https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://ru.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def rankeun(update, context):
    us = " ".join(context.args)
    response=requests.get('https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def rankbr(update, context):
    us = " ".join(context.args)
    response=requests.get('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def rankjp(update, context):
    us = " ".join(context.args)
    response=requests.get('https://jp1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://jp1.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def rankkr(update, context):
    us = " ".join(context.args)
    response=requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def rankla1(update, context):
    us = " ".join(context.args)
    response=requests.get('https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://la1.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def rankla2(update, context):
    us = " ".join(context.args)
    response=requests.get('https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://la2.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def rankna(update, context):
    us = " ".join(context.args)
    response=requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def rankoc(update, context):
    us = " ".join(context.args)
    response=requests.get('https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://oc1.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def ranktr(update, context):
    us = " ".join(context.args)
    response=requests.get('https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{us}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, us=us)).json()
    usernameToId=response['id']
    response=requests.get('https://tr1.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")

def usernameToId(update, context):
    context.user_data["user"] = update.message.text
    user=context.user_data["user"]
    reg=context.user_data["region"]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Now use a command to get your stats. Type /help for a list.")
    response=requests.get('https://{reg}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{user}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, user=user, reg=reg)).json()
    usernameToId=response['id']
    context.user_data["usernameToId"] = usernameToId

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('To obtain the rank, simply write /rank USERNAME, valid only for the EUW server. For other servers read at the end of this message*.' + "\n" + "\n" +
    "To get advanced statistics type /start and select your server. Then enter your username. After this you can use the following commands: " + "\n"
    "/elo to get the account rank" + "\n" + "/level to get the account level" + "\n" + "/winlose to get the number of wins and losses per queue" + "\n" + "\n" +
    "*To obtain rank in other regions the command is:" + "\n" + "/rankru 'username' for RU SERVER" + "\n" + "/rankeun 'username' for EUN SERVER"+ "\n" + "/rankbr 'username' for BR SERVER" + "\n"
    "/rankjp 'username' for JP SERVER" + "\n"+ "/rankkr 'username' for KR SERVER" + "\n" + "/rankla1 'username' for LA1 SERVER" + "\n" + "/rankla2 'username' for LA2 SERVER" + "\n"+ 
    "/rankna 'username' for NA SERVER" + "\n" + "/rankoc 'username' for OC SERVER" + "\n"+ "/ranktr 'username' for TR SERVER")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def elo(update, context):
    usernameToId = context.user_data["usernameToId"]
    reg=context.user_data["region"]
    response=requests.get('https://{reg}.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId, reg=reg)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP" + '\n'+
        response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": " + response[0]['tier'] + " " + response[0]['rank'] + " " + str(response[0]['leaguePoints']) + " LP")
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": " + response[1]['tier'] + " " + response[1]['rank'] + " " + str(response[1]['leaguePoints']) + " LP")
            except:
                update.message.reply_text("No rank.")


def level(update, context):
    user=context.user_data["user"]
    region=context.user_data["region"]
    response=requests.get('https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{user}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, user=user, region=region)).json()
    update.message.reply_text(user + ' account level is ' + str(response['summonerLevel']))

def winlose(update, context):
    usernameToId = context.user_data["usernameToId"]
    reg=context.user_data["region"]
    response=requests.get('https://{reg}.api.riotgames.com/lol/league/v4/entries/by-summoner/{usernameToId}?api_key={LOLKEY}'.format(LOLKEY=LOLKEY, usernameToId=usernameToId, reg=reg)).json()
    try:
        update.message.reply_text(response[0]['queueType'] + ": "+ "wins: " + str(response[0]['wins']) + " - losses: " + str(response[0]['losses']) + '\n' +
        response[1]['queueType'] + ": "+ "wins: " + str(response[1]['wins']) + " - losses: " + str(response[1]['losses']))
    except:
        try:
            update.message.reply_text(response[0]['queueType'] + ": "+ "wins: " + str(response[0]['wins']) + " - losses: " + str(response[0]['losses']))
        except:
            try:
                update.message.reply_text(response[1]['queueType'] + ": "+ "wins: " + str(response[1]['wins']) + " - losses: " + str(response[1]['losses']))
            except:
                update.message.reply_text("No stats.")


def unknown(update, context):
    #Comandi non validi
    context.bot.send_message(chat_id=update.effective_chat.id, text="Command not found!")


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater=Updater(token='', use_context=True)
    dispatcher=updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler("rank", rank))
    dispatcher.add_handler(CommandHandler("rankru", rankru))
    dispatcher.add_handler(CommandHandler("rankeun", rankeun))
    dispatcher.add_handler(CommandHandler("rankbr", rankbr))
    dispatcher.add_handler(CommandHandler("rankjp", rankjp))
    dispatcher.add_handler(CommandHandler("rankkr", rankkr))
    dispatcher.add_handler(CommandHandler("rankla1", rankla1))
    dispatcher.add_handler(CommandHandler("rankla2", rankla2))
    dispatcher.add_handler(CommandHandler("rankna", rankna))
    dispatcher.add_handler(CommandHandler("rankoc", rankoc))
    dispatcher.add_handler(CommandHandler("ranktr", ranktr))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('elo', elo))
    dispatcher.add_handler(CommandHandler('level', level))
    dispatcher.add_handler(CommandHandler('winlose', winlose))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(MessageHandler(Filters.text, usernameToId))
    dispatcher.add_error_handler(error)
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    #gestione comandi non esistenti, DA METTERE DOPO TUTTI GLI HANDLERS!!!!

    response=requests.get(url='https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Siramus?api_key={LOLKEY}'.format(LOLKEY=LOLKEY))
    print(response.status_code)
    
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
