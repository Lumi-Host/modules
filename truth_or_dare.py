import json
import random

import requests
from telethon.tl.types import Message

from .. import loader, utils
from ..inline.types import InlineCall


@loader.tds
class TruthOrDareMod(loader.Module):
    """Truth or dare? Play your favorite game from inside the Telegram (en/ru)"""

    strings = {
        "name": "TruthOrDare",
        "choose_language": "👩‍🎤 <b>Choose language</b>",
        "truth_or_dare_uk": "🔴 <b>Правда</b> чи <b>Дія</b>? 🔵",
        "truth_or_dare_en": "🔴 <b>Truth</b> or <b>Dare</b>? 🔵",
        "truth_uk": "🤵‍♀️ Правда",
        "dare_uk": "🥷 Дія",
        "truth_en": "🤵‍♀️ Truth",
        "dare_en": "🥷 Dare",
        "language_saved_uk": "🇺🇦 Мовy збереженo",
        "language_saved_en": "🇬🇧 Language saved",
        "classic_uk": "🙂 Класичний",
        "classic_en": "🙂 Classic",
        "kids_uk": "👨‍👦 Для дітей",
        "kids_en": "👨‍👦 Kids",
        "party_uk": "🥳 Вечірка",
        "party_en": "🥳 Party",
        "hot_ua": "❤️‍🔥 Палке",
        "hot_en": "❤️‍🔥 Hot",
        "mixed_uk": "🔀 Різне",
        "mixed_en": "🔀 Mixed",
        "category_uk": "😇 <b>Вибери категорію гри:</b>",
        "category_en": "😇 <b>Choose game category:</b>",
        "args": "▫️ <code>.todlang en/uk</code>",
    }

    async def client_ready(self, client, db):
        if self.get("lang") in {"uk", "en"}:
            self._update_lang()

    async def truth_or_dare(self, tod: str, category: str) -> str:
        return random.choice(
            (
                await utils.run_sync(
                    requests.post,
                    "https://psycatgames.com/api/tod-v2/",
                    headers={
                        "referer": "https://psycatgames.com/app/truth-or-dare/?utm_campaign=tod_website&utm_source=tod_en&utm_medium=website"
                    },
                    data=json.dumps(
                        {
                            "id": "truth-or-dare",
                            "language": self.get("lang"),
                            "category": category,
                            "type": tod,
                        }
                    ),
                )
            ).json()["results"]
        )

    def _update_lang(self):
        self._markup = [
            [
                {
                    "text": self.strings(f"classic_{self.get('lang')}"),
                    "callback": self._inline_start,
                    "args": ("classic",),
                },
                {
                    "text": self.strings(f"kids_{self.get('lang')}"),
                    "callback": self._inline_start,
                    "args": ("kids",),
                },
            ],
            [
                {
                    "text": self.strings(f"party_{self.get('lang')}"),
                    "callback": self._inline_start,
                    "args": ("party",),
                },
                {
                    "text": self.strings(f"hot_{self.get('lang')}"),
                    "callback": self._inline_start,
                    "args": ("hot",),
                },
            ],
            [
                {
                    "text": self.strings(f"mixed_{self.get('lang')}"),
                    "callback": self._inline_start,
                    "args": ("mixed",),
                },
            ],
        ]

    async def _inline_set_language(self, call: InlineCall, lang: str):
        self.set("lang", lang)
        await call.answer(self.strings(f"language_saved_{lang}"), show_alert=True)
        self._update_lang()
        await call.edit(
            self.strings(f"truth_or_dare_{self.get('lang')}"), reply_markup=self._markup
        )

    async def _inline_process(
        self,
        call: InlineCall,
        action: str,
        category: str,
    ):
        action_babel = self.strings(f"{action}_{self.get('lang')}")
        await call.edit(
            f"<b>{action_babel}</b>:\n\n{await self.truth_or_dare(action, category)}",
            reply_markup=[
                {
                    "text": self.strings(f"truth_{self.get('lang')}"),
                    "callback": self._inline_process,
                    "args": ("truth", category),
                },
                {
                    "text": self.strings(f"dare_{self.get('lang')}"),
                    "callback": self._inline_process,
                    "args": ("dare", category),
                },
            ],
        )

    async def _inline_start(self, call: InlineCall, category: str):
        await call.edit(
            self.strings(f"truth_or_dare_{self.get('lang')}"),
            reply_markup=[
                {
                    "text": self.strings(f"truth_{self.get('lang')}"),
                    "callback": self._inline_process,
                    "args": ("truth", category),
                },
                {
                    "text": self.strings(f"dare_{self.get('lang')}"),
                    "callback": self._inline_process,
                    "args": ("dare", category),
                },
            ],
        )

    async def todcmd(self, message: Message):
        """Start new truth or dare game"""
        if not self.get("lang"):
            await self.inline.form(
                self.strings("choose_language"),
                message=message,
                reply_markup=[
                    {
                        "text": "🇺🇦 UA",
                        "callback": self._inline_set_language,
                        "args": ("uk",),
                    },
                    {
                        "text": "🇬🇧 English",
                        "callback": self._inline_set_language,
                        "args": ("en",),
                    },
                ],
            )
            return

        await self.inline.form(
            self.strings(f"category_{self.get('lang')}"),
            message=message,
            reply_markup=self._markup,
            disable_security=True,
        )

    async def todlangcmd(self, message: Message):
        """[en/uk] - Change language"""
        args = utils.get_args_raw(message).lower().strip()
        if args not in {"uk", "en"}:
            await utils.answer(message, self.strings("args"))
            return

        self.set("lang", args)
        self._update_lang()

        ans = self.strings(f"language_saved_{args}")
        await utils.answer(message, f"<b>{ans}</b>")
