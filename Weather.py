__version__ = (1, 1, 0)

# scope: inline_content
# requires: requests
# meta developer: @authorche
# meta pic: https://www.google.com/search?q=weather+logo&tbm=isch&ved=2ahUKEwiys67n2aP-AhWMh_0HHYTPB3kQ2-cCegQIABAC&oq=weather+logo&gs_lcp=ChJtb2JpbGUtZ3dzLXdpei1pbWcQAzIFCAAQgAQyBQgAEIAEMgQIABAeMgQIABAeMgQIABAeOgQIIxAnOgYIABAHEB5Qow9Y-hZglRloAHAAeACAAdUBiAGDB5IBBTAuNC4xmAEAoAEBwAEB&sclient=mobile-gws-wiz-img&ei=0U02ZPKGJYyP9u8PhJ-fyAc&bih=813&biw=424&client=ms-android-meizu&prmd=ivsn#imgrc=lr3pl-R_YP76qM&lnspr=W10=
import requests
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineKeyboardButton,
    InputTextMessageContent,
)
from urllib.parse import quote_plus
from telethon.tl.types import Message
from telethon.tl.functions.channels import JoinChannelRequest
from ..inline.types import InlineQuery
from ..utils import rand
from .. import loader  # noqa
from .. import utils  # noqa
import logging
import re

logger = logging.getLogger(__name__)

n = '\n'
ua = "йцукенгшщзхфіївапролджєячсмитьбю"

def escape_ansi(line):
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)


class WeatherMod(loader.Module):
    """Weather module"""
    id = 17
    strings = {
        "name": "Weather",
    }

    async def weathercitycmd(self, message: Message) -> None:
        """Set default city for forecast"""
        if args := utils.get_args_raw(message):
            self.db.set(self.strings['name'], 'city', args)
        await utils.answer(message, f"<b>🏙 Your current city: "
                                    f"<code>{self.db.get(self.strings['name'], 'city', '🚫 Not specified')}</code></b>")
        return

    async def weathercmd(self, message: Message) -> None:
        """Current forecast for provided city"""
        city = utils.get_args_raw(message)
        if not city:
            city = self.db.get(self.strings['name'], 'city', "")
        lang = 'ua' if city and city[0].lower() in uk else 'en'
        req = requests.get(f"https://wttr.in/{city}?m&T&lang={lang}")
        await utils.answer(message, f'<code>{n.join(req.text.splitlines()[:7])}</code>')

    async def weather_inline_handler(self, query: InlineQuery) -> None:
        """Подивитися погоду"""
        args = query.args
        if not args:
            args = self.db.get(self.strings['name'], 'city', "")
        if not args:
            return
        # req = requests.get(f"https://wttr.in/{quote_plus(args)}?format=j1").json()
        lang = 'uk' if args and args[0].lower() in ua else 'en'
        req = requests.get(f"https://wttr.in/{quote_plus(args)}?format=3")
        await query.answer(
            [
                InlineQueryResultArticle(
                    id=rand(20),
                    title=f"Прогноз погоди в місті {args}",
                    description=req.text,
                    # thumb_url="https://i.ytimg.com/vi/IMLwb8DIksk/maxresdefault.jpg",
                    input_message_content=InputTextMessageContent(
                        f'<code>{n.join(requests.get(f"https://wttr.in/{args}?m&T&lang={lang}").text.splitlines()[:7])}</code>',
                        parse_mode="HTML",
                    ),
                )
            ],
            cache_time=0,
        )
