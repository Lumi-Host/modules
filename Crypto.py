__version__ = (0, 0, 4)
#            2022
# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @AuthorChe

from .. import loader, utils
from telethon.tl.types import Message
import requests
import random as r

class MyCryptoManagerMod(loader.Module):
    """Awesome cryptocurrency viewer"""

    strings = {
        "name": "Crypto",
        "inc_args": "<b>🐳 Incorrect args</b>",
        "keyerror": "🗿 <b>Maybe the coin is not in the site database or you typed the wrong name.</b>",
        "okey": "<b>👯 Successfully. Current default valute: {}</b>"
    }
    strings_ru = {
        "inc_args": "<b>🐳 Неккоректные аргументы</b>",
        "keyerror": "🗿 <b>Возможно монеты нету в базе данных сайта, или вы ввели неккоректное название.</b>",
        "okey": "<b>👯 Успешно. Текущая стандартная валюта: {}</b>"
    }

    async def defvaluecmd(self, message: Message):
        """set a default valute"""

        args = utils.get_args_raw(message)
        self.db.set("defaultvalute", "val", args)
        await utils.answer(message, self.strings('okey').format(args))

    async def cryptocmd(self, message: Message):
        "use .crypto <count (float or int)> <coin name>."
        args = utils.get_args_raw(message)
        tray = self.db.get("defaultvalute", "val", args)
        if tray == "":
            tray = "btc"
        if not args:
            args = "1" + " " + str(tray)

        args_list = args.split(" ")
        try:
            if len(args_list) == 1 and isinstance(float(args_list[0]), float) == True:
                args_list.append(str(tray))
        except Exception:
            args_list = ["1", args_list[0]]
        coin = args_list[1].upper()
        api = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms=USD,RUB,UAH,KZT"
        ).json()
        smile = "💷 💶 💴 💵".split(" ")
        smiles = r.choice(smile)

        try:
            try:
                count = float(args_list[0])
                form = (
                    "AuthorCrypto💻\n"
                    "{} <b>{} {}</b>\n"
                    "🇺🇦 <code>{}₴</code>\n"
                    "🇺🇲 <code>{}$</code>\n"
                    "🇰🇿 <code>{}₸</code>\n"
                    "🏳‍⚧ <code>{}₽</code>"
                   
                ).format(
                    smiles,
                    count,
                    coin,
                    round(api["UAH"] * count, 2),
                    round(api["USD"] * count, 2),
                    round(api["KZT"] * count, 2),
                    round(api["RUB"] * count, 2),
                )

         
                await self.inline.form(
                    message=message,
                    text = form,
                )
            except KeyError:
                await utils.answer(message, self.strings("keyerror"))
        except ValueError:
            await utils.answer(message, self.strings("inc_args"))
