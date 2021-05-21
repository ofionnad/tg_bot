from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters
from telegram import run_async
import config

TOKEN = config.TOKEN
CHART = config.CHART
BSC = config.BSC
CON = config.CON

@run_async
def send_async(context, *args, **kwargs) -> None:
    context.bot.send_message(*args, **kwargs)

def chart(update: Update, context: CallbackContext):
    update.message.reply_text(
        "https://dex.guru/token/{}".format(CHART)
    )

def bsc(update: Update, context: CallbackContext):
    update.message.reply_text(
        "https://bscscan.com/token/{}".format(BSC)
    )


def contract(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Contract Address:\n{} \n\nREMEMBER: \nUse Version 1 of PCS \n\nset 11.5% slippage".format(CON)
    )


def error_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Apologies, I am currently not working.\nPlease try again later.\n\nOr buy some $WAIV!!!"
    )

def text_filter(update: Update, context: CallbackContext):
	words = update.message.text.lower().split()
	prizeword = "elon"
	if prizeword in words:
		update.message.reply_text("WE HAVE A GIVEAWAY WINNER!!\nThe word was \n\n{}\n\n Please contact an admin to collect your prize!\n\n @Waivmeister".format(prizeword))
		dp.remove_handler(msg_handler)

def welcome(update:Update, context:CallbackContext, new_member) -> None:
    """ Welcomes a user to the chat """

    chat_id = update.message.chat.id

    text = "Welcome @{}! Thanks for joining the xxxxxxxxx \
            community! Read pinned messages to get up to \
            speed and feel free to ask any questions \
            you have here. \U0001F601 \U0001F680".format(new_member.username)

    send_async(context, chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)


def empty_msg(update: Update, context:CallbackContext):

    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            return welcome(update, context, new_member)

if __name__ == "__main__":

    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("chart", chart))
    dp.add_handler(CommandHandler("contract", contract))
    dp.add_handler(CommandHandler("bsc", bsc))
    msg_handler = MessageHandler(Filters.update.message, text_filter)
    #dp.add_handler(msg_handler) #you just uncomment this line to add in the giveaway code
    dp.add_handler(MessageHandler(Filters.status_update, empty_msg)) #this can handle other empty message statuses but I just filter for new members.
    dp.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()