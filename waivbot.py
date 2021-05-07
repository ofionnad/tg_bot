from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import config

TOKEN = config.TOKEN


def chart(update: Update, context: CallbackContext):
    update.message.reply_text(
        "https://bsc.tools/pair-explorer/0x7704728b33eba47bf948fdbcb2cb8d05667157c9"
    )


def bsc(update: Update, context: CallbackContext):
    update.message.reply_text(
        "https://bscscan.com/token/0xAA5c91F3df88B8B3863d0899bcA33E70482beD2A"
    )


def contract(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Contract Address:\n0xAA5c91F3df88B8B3863d0899bcA33E70482beD2A \n\nREMEMBER: \nUse Version 1 of PCS \n\nset 11.5% slippage"
    )


def error_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Apologies, I am currently not working.\nPlease try again later."
    )


if __name__ == "__main__":

    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("chart", chart))
    dp.add_handler(CommandHandler("contract", contract))
    dp.add_handler(CommandHandler("bsc", bsc))
    dp.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()
