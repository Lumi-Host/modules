import abc
import time

from aiogram.types import Message as AiogramMessage
from telethon.utils import get_display_name

from .. import loader, utils
from ..inline.types import InlineCall


@loader.tds
class MenuBotMod(loader.Module):
    """Simple menu for bot"""

    __metaclass__ = abc.ABCMeta

    strings = {
        "name": "Menu bot",
        "/nometa_en": (
            "👨‍🎓 <b><u>Internet-talk rules:</u></b>\n\n"
            "<b>🚫 Do <u>not</u> send just 'Hello'</b>\n"
            "<b>🚫 Do <u>not</u> advertise</b>\n"
            "<b>🚫 Do <u>not</u> insult</b>\n"
            "<b>🚫 Do <u>not</u> split message</b>\n"
            "<b>✅ Write your question in one message</b>"    
        ),
        "/nometa":(
        "👨‍🎓<b><u>Правила спілкування в Інтернеті:</u></b>\n\n"
"🚫 <b>Не надсилайте просто `Привіт`</b>"
"🚫 <b>Не рекламуйте нічого</b>"
"🚫 <b>Не займайтесь булінгом</b>"
"🚫 <b>Не розділяйте повідомлення на шматочки</b>"
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
"<code>/donate</code> — <b><i>Donate❤️</i></b>\n"
"<code>/menu</code> — <i>Меню бота</i>\n\n"
"<b>ℹ️ Доступні команди inline:</b>\n"
"🎹 <code>@authorche_bot choice</code> - [аргументи, розділені комою] - Зробити вибір\n"
"🎹 <code>@authorche_bot coin</code> - Орел чи Решка?\n"
"🎹 <code>@authorche_bot random</code> - [Число] - Надіслати випадкове число менше вказаного\n"
"🎹 <code>@authorche_bot info</code> - Подивитися інформацію про бота.\n"
"🎹 <code>@authorche_bot hide</code> - Створює спойлери, які доступні тільки окремим користувачам (hide @usеrname message)\n"
"🎹 <code>@authorche_bot weather</code> - Подивитися погоду(weather місто)\n"
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
        if message.text == "/menu":
            await message.answer(
                self.strings("/menu").format(self._name),
            )
        elif message.text == "/nometa_en":
            await message.answer(self.strings("/nometa_en"))