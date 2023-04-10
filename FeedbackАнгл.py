                               
# meta developer: @Vadym_Yem

__version__ = (4, 1, 5)

import logging, time
from telethon.utils import get_display_name
from aiogram.types import Message as AiogramMessage
from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)


@loader.unrestricted
@loader.ratelimit
@loader.tds
class FeedbackBotEnMod(loader.Module):

    strings = {
        "name": "FeedbackEn",
        "start_en": ("✌️ Hi, welcome to the feedback menu"),
        "fb_message_en": "📝 Take to send message",
        "wait_en": "⏳ You can send next message in {} second(-s)",
        "feedback_en": "📝 Write 1 message",
        "sent_en": "📩 Message sent",
        "banned_en": "🚫 You are banned",
        "user_banned_en": "🚫 {} is banned",
         "/nometa": (
            "👨‍🎓 <b><u>Internet-talk rules:</u></b>\n\n"
            "<b>🚫 Do <u>not</u> send just 'Hello'</b>\n"
            "<b>🚫 Do <u>not</u> advertise</b>\n"
            "<b>🚫 Do <u>not</u> insult</b>\n"
            "<b>🚫 Do <u>not</u> split message</b>\n"
            "<b>✅ Write your question in one message</b>"
        ),
        "enter_message_en": "✍️ <b>Enter your message here</b>",
        "sent_en": "✅ <b>Your message has been sent to owner</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "ratelimit",
            "1",
            lambda: "Rate limit(in minutes)",
        )
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self._client = client

        self._name = utils.escape_html(get_display_name(await client.get_me()))

        self._ratelimit = {}
        self._ban_list = []

        self.__doc__ = "Module from add feedback bot 👨‍💻\n\n" \
        "📝 Dev: @Vadym_Yem\n" \
        "📥 Source: @Vadym_Yem\n" \
        f"🏔 Feedback command: /feedback_en\n\n" \
        


    async def aiogram_watcher(self, message: AiogramMessage):
        if message.text == "/feedback_en":
            if str(message.from_user.id) in str(self._ban_list):
                return await message.answer(
                    self.strings("banned_en")
                )
            _markup = self.inline.generate_markup(
                {"text": self.strings("fb_message_en"), "data": "fb_message_en"}
            )
            await message.answer(
                self.strings("start_en").format(self._name),
                reply_markup=_markup,
            )
        if self.inline.gs(message.from_user.id) == "fb_send_message_en":
            await self.inline.bot.forward_message(
                self._tg_id,
                message.chat.id,
                message.message_id,
            )
            _markup = self.inline.generate_markup(
                {"text": "🚫 Ban", "data": f"fb_ban_en/{message.from_user.id}"}
            )
            await self.inline.bot.send_message(
                self._tg_id,
                f"{message.chat.id}",
                reply_markup=_markup,
            )
            await message.answer(self.strings("sent_en"))
            self._ratelimit[message.from_user.id] = time.time() + self.config["ratelimit"] * 60
            self.inline.ss(message.from_user.id, False)

    @loader.inline_everyone
    async def feedback_en_callback_handler(self, call: InlineCall):
        if call.data == "fb_cancel_en":
            self.inline.ss(call.from_user.id, False)
            await self.inline.bot.delete_message(
                call.message.chat.id,
                call.message.message_id,
            )
            return
        if call.data.split('/')[0] == "fb_ban_en":
            fb_ban_en_id = call.data.split('/')[1]
            if str(fb_ban_en_id) in str(self._ban_list):
                pass
            else:
                self._ban_list.append(fb_ban_en_id)
                await call.answer(self.strings("user_banned_en").format(fb_ban_en_id))

        if call.data != "fb_message_en":
            return

        if str(call.from_user.id) in str(self._ban_list):
            await call.answer(
                self.strings("banned_en"),
                show_alert=True,
            )

        if (
            call.from_user.id in self._ratelimit
            and self._ratelimit[call.from_user.id] > time.time()
        ):
            await call.answer(
                self.strings("wait_en").format(self._ratelimit[call.from_user.id] - time.time()),
                show_alert=True,
            )
            return

        self.inline.ss(call.from_user.id, "fb_send_message_en")
        
        await call.answer(
            self.strings("feedback_en").format(self._name, self.config["ratelimit"]),
        )
