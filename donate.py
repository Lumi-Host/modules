import abc
import time

from aiogram.types import Message as AiogramMessage
from telethon.utils import get_display_name

from .. import loader, utils
from ..inline.types import InlineCall


@loader.tds
class DonateBotMod(loader.Module):
    """Simple donate for bot"""

    __metaclass__ = abc.ABCMeta

    strings = {
        "name": "DonateBot",
        "/donate": (
            "So you want to donate? Amazing!"
'You can donate on <a href="https://www.privat24.ua/rd/transfer_to_card/?hash=rd%2Ftransfer_to_card%2F%7B%22from%22%3A%22%22%2C%22to%22%3A%224149499388981035%22%2C%22amt%22%3A%22100%22%2C%22ccy%22%3A%22UAH%22%7D">PrivatBank</a>, or sent money to 4149499388981035\n' 
'You can join to <a href="https://t.me/AuthorChe">AuthorChe`s</a>.'
'This project is entirely run by Author, and server fees aren`t cheap, so I thank you for your support!'
        ),
        "/nometa":(
        "👨‍🎓<b><u>Правила спілкування в Інтернеті:</u></b>\n\n"
"🚫 <b>Не надсилайте просто `Привіт`</b>\n"
"🚫 <b>Не рекламуйте нічого</b>\n"
"🚫 <b>Не займайтесь булінгом</b>\n"
"🚫 <b>Не розділяйте повідомлення на шматочки</b>\n"
"✅ <b>Напишіть своє запитання одним повідомленням.</b>"
        ),
        
        "/menu": (
        "✌️<b>Привіт, вітаю в меню\n"
        "Команди які ви можете використовувати</b>:\n"
        "<code>/start</code> — <i>щоб перезапустити бота</i>\n"
"<code>/feedback</code> — <i>UA🇺🇦 feedback (зворотній зв`язок)</i>\n"
"<code>/feedback_en</code> — <i>EN🇬🇧 feedback</i>\n"
"<code>/nometa_en</code> — <i>Internet talk rules</i>\n"
"<code>/nometa</code> — <i>Правила спілкування в Інтернеті</i>\n"
"<code>/menu</code> — <i>Меню бота</i>\n\n"
"<b>ℹ️ Доступні команди inline:</b>\n"
"🎹 <code>@authorche_bot choice</code> - [аргументи, розділені комою] - Зробити вибір\n"
"🎹 <code>@authorche_bot coin</code> - Орел чи Решка?\n"
"🎹 <code>@authorche_bot random</code> - [Число] - Надіслати випадкове число менше вказаного\n"
"🎹 <code>@authorche_bot info</code> - Подивитися інформацію про бота.\n"
"🎹 <code>@authorche_bot hide</code> - Створює спойлери, які доступні тільки окремим користувачам (hide @usеrname message)\n"
"🎹 <code>@authorche_bot weather</code> - Подивитися погоду\n"
"🎹 <code>@authorche_bot lr</code> - Створити гарне приховане повідомлення (lr text)\n"
"🎹 <code>@authorche_bot ping</code> - Перевірка швидкості бота\n"
"🎹 <code>@authorche_bot tl</code> - Для розробників телеграму"
        ),
    }
    
    async def client_ready(self):
        self._name = utils.escape_html(get_display_name(self._client.hikka_me))
        

        self.__doc__ = (
            "Menu for bot\n"
        )

    async def aiogram_watcher(self, message: AiogramMessage):
        if message.text == "/donate":
            await message.answer(
                self.strings("/donate").format(self._name),
            )
        elif message.text == "/nometa":
            await message.answer(self.strings("/nometa"))
