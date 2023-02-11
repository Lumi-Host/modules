import requests
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привіт! Я пошуковий бот української Вікіпедії. Що я можу допомогти тобі знайти сьогодні?\n\nВід @AuthorChe")

def search(update, context):
    query = " ".join(context.args)
    wikipedia_api = "https://uk.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": query,
        "exintro": "",
        "explaintext": ""
    }
    response = requests.get(wikipedia_api, params=params).json()
    page_id = list(response["query"]["pages"].keys())[0]
    if page_id == "-1":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Вибачте, я нічого не знайшов у Вікіпедії щодо цього.")
    else:
        extract = response["query"]["pages"][page_id]["extract"]
        context.bot.send_message(chat_id=update.effective_chat.id, text=extract)

def main():
    updater = Updater("5858139983:AAFT_STt2FchoHPzqrCepkp8jGUZEv7F3R0", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("search", search))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
