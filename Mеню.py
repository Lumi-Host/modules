__version__ = (2, 0, 1)

import logging
from aiogram.types import Message as AiogramMessage
from .. import loader
from ..inline.types import InlineCall

import requests

logger = logging.getLogger(__name__)


@loader.tds
class CommandsMod(loader.Module):

    strings = {"name": "Command's"}

    async def client_ready(self):
        self.__doc__ = (
            "Модуль для меню"
        )
    async def aiogram_watcher(self, message: AiogramMessage):
        if self._client._tg_id == message.chat.id and message.text:
            if message.text == "/menu":
                await self.inline.bot.send_message(
                    self._tg_id,
"""
😎✌️<b>Привіт, вітаю в меню.\nКоманди які ви можете використовувати</b>:<i>\n<code>/start</code> — щоб перезапустити бота\n<code>/feedback</code> — UA🇺🇦 Feedback (зворотній зв'язок)\n<code>/feedback_en</code> — EN🇬🇧 Feedback\n<code>/manga</code> — Читати мангу в боті(російською)
<code>/nometa</code> — Правила спілкування в Інтернеті
<code>/menu</code> — Меню бота</i>\n\n
<b>ℹ️ Доступні команди inline:</b>\n🎹 <code>@authorche_bot choice</code> - [аргументи, розділені комою] - Зробити вибір\n
🎹 <code>@authorche_bot coin</code> - Орел чи Решка?\n
🎹 <code>@authorche_bot random</code> - [Число] - Надіслати випадкове число менше вказаного\n
🎹 <code>@authorche_bot info</code> - Подивитися інформацію про бота.\n
🎹 <code>@authorche_bot hide</code> - Створює спойлери, які доступні тільки окремим користувачам (hide @usеrname message)\n
🎹 <code>@authorche_bot weather</code> - Подивитися погоду\n
🎹 <code>@authorche_bot lr</code> - Створити гарне приховане повідомлення (lr text)\n
🎹 <code>@authorche_bot ping</code> - Перевірка швидкості бота\n
🎹 <code>@authorche_bot tl</code> - Для розробників телеграму
"""
                )
                
            if message.text == "/nometa":
                await self.inline.bot.send_message(
                    self._tg_id,
"""👨‍🎓Правила спілкування в Інтернеті:
🚫 Не надсилайте просто "Привіт"
🚫 Не рекламуйте нічого
🚫 Не займайтесь булінгом
🚫 Не розділяйте повідомлення на шматочки
✅ Напишіть своє запитання одним повідомленням.
"""
                 )