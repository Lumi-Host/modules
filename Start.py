import abc
import time

from aiogram.types import Message as AiogramMessage
from telethon.utils import get_display_name

from .. import loader, utils
from ..inline.types import InlineCall


@loader.tds
class StartBotMod(loader.Module):
    """Simple menu for bot"""

    __metaclass__ = abc.ABCMeta

    strings = {
        "name": "Start bot",
        "/restart": (
         "✌️<b>Привіт, вітаю вас тут\n"
        "Це бот від каналу @AuthorChe</b>:\n\n"
        "Скористайтеся /menu для перегляду функціоналу"  
        ),
        
        "/author":(
        "Власником боту є @Vadym_Yem. Бот є повністю безкоштовним та не містить жодної реклами. Ціллю створення є бажання спростити користування месенджером Telegram. Ви можете підтримати проект (/donate)"
        ),                
    }
    
    async def client_ready(self):
        self._name = utils.escape_html(get_display_name(self._client.hikka_me))
        

        self.__doc__ = (
            "Menu for bot\n"
        )

    async def aiogram_watcher(self, message: AiogramMessage):
        if message.text == "/restart":
            await message.answer(
                self.strings("/restart").format(self._name),
            )
        elif message.text == "/author":
            await message.answer(self.strings("/author"))