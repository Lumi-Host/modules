
__version__ = (1, 0, 2)
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @vadym_yem
# scope: inline
# scope: acbot_only
# scope: acbot_min 1.2.10

from .. import loader, utils
from ..inline.types import InlineCall, InlineQuery
from telethon.tl.types import Message


@loader.tds
class LongReadMod(loader.Module):
    """Приховує текст під гарну кнопочку"""

    strings = {
        "name": "LongRead",
        "no_text": "🚫 <b>Please specify the text to be hidden</b>",
        "longread": (
            "🔥 <b>Interesting message for you</b>\n<i>Click on the button to read it :) \nButton"
            " is active for 6 hours</i>"
        ),
        "_cmd_doc_lr": "<text> - hide text under pretty button"
        "_cls_doc": "Hides your text under a nice button",
    }

    strings_ua = {
        "no_text": "🚫 <b>Будь ласка, вкажіть текст, що треба приховати</b>",
        "longread": (
            "🔥 <b>Для вас цікаве повідомлення</b>\n<i>Натисніть на кнопку, щоб прочитати його :) \nКнопка"
            " активна протягом 6 годин</i>"
        ),
        "_cmd_doc_lr": "<text> - приховати текст під гарну кнопочку",
        "_cls_doc": "Ховає ваш текст під гарну кнопочку",
    }

    async def lrcmd(self, message: Message):
        """<text> - Create new hidden message"""
        args = utils.get_args_raw(message)
        if not args:
            return

        await self.inline.form(
            self.strings("longread"),
            message,
            reply_markup={
                "text": "📖 Переглянути",
                "callback": self._handler,
                "args": (args,),
            },
            disable_security=True,
        )

    async def lr_inline_handler(self, query: InlineQuery):
        """Create new hidden message"""
        text = query.args

        if not text:
            return await query.e400()

        return {
            "title": "Create new longread",
            "description": "ℹ This will create button-spoiler",
            "thumb": "https://img.icons8.com/external-wanicon-flat-wanicon/64/000000/external-read-free-time-wanicon-flat-wanicon.png",
            "message": self.strings("longread"),
            "reply_markup": {
                "text": "📖 Переглянути",
                "callback": self._handler,
                "args": (text,),
                "disable_security": True,
            },
        }

    async def _handler(self, call: InlineCall, text: str):
        """Process button presses"""
        await call.edit(text)
        await call.answer()
