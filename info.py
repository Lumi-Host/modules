__version__ = (2, 5, 0)

#              © Copyright 2022
#
# https://t.me/AuthorChe
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @AuthorChe

# scope: inline
# scope: acbot_only
# scope: acbot_min 1.1.27

import logging
import git

from telethon.tl.types import Message
from telethon.utils import get_display_name

from .. import loader, main, utils, version
import datetime
import time
from ..inline.types import InlineQuery

logger = logging.getLogger(__name__)


@loader.tds
class acbotInfoMod(loader.Module):
    """Show 𝙰𝚞𝚝𝚑𝚘𝚛𝙲𝚑𝚎'𝚜 info"""

    strings = {
        "name": "Info",
        "owner": "Owner",
        "version": "Version",
        "build": "Build",
        "prefix": "Prefix",
        "branch": "Branch",
        "cpu_usage": "CPU usage",
        "ram_usage": "RAM usage",
        "send_info": "Send bot info.",
        "description": "ℹ This will not compromise any sensitive info.",
        "up-to-date": "😌 Up-to-date.",
        "update_required": "😕 Update required </b><code>.update</code><b>",
        "_cfg_cst_msg": "Custom message for info. May contain {me}, {version}, {build}, {prefix}, {platform}, {upd} keywords.",
        "_cfg_cst_btn": "Custom button. Leave empty to remove button.",
        "_cfg_cst_bnr": "Custom Banner.",
        "_cfg_cst_frmt": "Custom fileformat for Banner.",
        "_cfg_banner": "Set `True` in order to disable an media banner.",
        "_cfg_inline_banner": "Set `True` in order to disable an inline media banner.",
    }

    strings_ua = {
        "owner": "Власник",
        "version": "Версiя",
        "build": "Збірка",
        "prefix": "Префікс",
        "branch": "Гілка",
        "cpu_usage": "використання CPU",
        "ram_usage": "використання RAM",
        "send_info": "Send bot info.",
        "description": "ℹ Це не розкриє особистої інформації :)",
        "_ihandle_doc_info": "Send bot info.",
        "up-to-date": "😌 Актуальна версия.",
        "update_required": "😕 Потрібне оновлення </b><code>.update</code><b>",
        "_cfg_cst_msg": "Кастом текст повідомлення в info. Може мати ключові слова {me}, {version}, {build}, {prefix}, {platform}, {cpu_usage}, {ram_usage}, {branch}",
        "_cfg_cst_btn": "Кастом кнопка повідомлення в info. Залиш пустим, щоб при прибрати.",
        "_cfg_cst_bnr": "Кастом банер.",
        "_cfg_cst_frmt": "Кастом формат файлу для банера.",
        "_cfg_banner": "Постав `True`, щоб вимкнути банер-картинку.",
        "_cfg_inline_banner": "Встановіть `True`, щоб відключити встроєний медіа-банер",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "custom_message",
                "no",
                doc=lambda: self.strings("_cfg_cst_msg"),
            ),
            loader.ConfigValue(
                "custom_banner",
                "https://imgur.com/Ze2TtW3",
                lambda: self.strings("_cfg_cst_bnr"),
            ),
            loader.ConfigValue(
                "custom_format",
                "photo",
                lambda: self.strings("_cfg_cst_frmt"),
                validator=loader.validators.Choice(["photo", "video", "audio", "gif"]),
            ),
            loader.ConfigValue(
                "disable_banner",
                False,
                lambda: self.strings("_cfg_banner"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "disable_inline_banner",
                False,
                lambda: self.strings("_cfg_inline_banner"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "timezone",
                "+3",
                lambda: self.strings("_cfg_time"),
            ),
            loader.ConfigValue(
                "close_btn",
                "🔻Close",
                lambda: self.strings("_cfg_close"),
            ),
            loader.ConfigValue(
                "custom_button1",
                ["AuthorChe✍️", "https://t.me/AuthorChe"],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button2",
                [],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button3",
                [],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button4",
                ["AuthorChe✍️", "https://t.me/AuthorChe"],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button5",
                ["AuthorChe✍️", "https://t.me/AuthorChe"],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button6",
                ["AuthorChe✍️", "https://t.me/AuthorChe"],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button7",
                [],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button8",
                [],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button9",
                [],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button10",
                [],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button11",
                [],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
            loader.ConfigValue(
                "custom_button12",
                [],
                lambda: self.strings("_cfg_cst_btn"),
                validator=loader.validators.Series(min_len=0, max_len=2),
            ),
        )

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self._me = await client.get_me()

    def _render_info(self) -> str:
        ver = utils.get_git_hash() or "Unknown"

        try:
            repo = git.Repo()
            diff = repo.git.log(["HEAD..origin/master", "--oneline"])
            upd = (
                self.strings("update_required") if diff else self.strings("up-to-date")
            )
        except Exception:
            upd = ""

        me = f'<b><a href="tg://user?id={self._me.id}">{utils.escape_html(get_display_name(self._me))}</a></b>'
        version = f'<i>{".".join(list(map(str, list(main.__version__))))}</i>'
        build = f'<a href="https://github.com/VadymYem/AuthorBot/commit/{ver}">#{ver[:8]}</a>'  # fmt: skip
        prefix = f"«<code>{utils.escape_html(self.get_prefix())}</code>»"
        platform = utils.get_named_platform()
        uptime = utils.formatted_uptime()
        offset = datetime.timedelta(hours=self.config["timezone"])
        tz = datetime.timezone(offset)
        time1 = datetime.datetime.now(tz)
        time = time1.strftime("%H:%M:%S")
        cpu_usage=utils.get_cpu_usage(),
        ram_usage=f"{utils.get_ram_usage()} MB",
        branch=version.branch,
            )
            if self.config["custom_message"]
            else (
                f'<b>{{}}</b>\n\n<b>{{}} {self.strings("owner")}:</b> {me}\n\n<b>{{}}'
                f" {self.strings('version')}:</b> {_version} {build}\n<b>{{}}"
                f" {self.strings('branch')}:"
                f"</b> <code>{version.branch}</code>\n{upd}\n\n<b>{{}}"
                f" {self.strings('prefix')}:</b> {prefix}\n<b>{{}}"
                f" {self.strings('uptime')}:"
                f"</b> {utils.formatted_uptime()}\n\n<b>{{}}"
                f" {self.strings('cpu_usage')}:"
                f"</b> <i>~{utils.get_cpu_usage()} %</i>\n<b>{{}}"
                f" {self.strings('ram_usage')}:"
                f"</b> <i>~{utils.get_ram_usage()} MB</i>\n<b>{{}}</b>"
            ).format(
                *map(
                    lambda x: utils.remove_html(x) if inline else x,
                    (
                        utils.get_platform_emoji()
                        if self._client.acbot_me.premium and not inline
                   else "𝙰𝚞𝚝𝚑𝚘𝚛𝙲𝚑𝚎'𝚜✍️",
                        "😎",
                        "💫",
                        "🌳",
                        "⌨️",
                        "⌛️",
                        "⚡️",
                        "💼",
                        platform,
                    ),
                )
            )
        )

    def _get_mark(self, btn_count):
        btn_count = str(btn_count)
        return (
            {
                "text": self.config[f"custom_button{btn_count}"][0],
                "url": self.config[f"custom_button{btn_count}"][1],
            }
            if self.config[f"custom_button{btn_count}"]
            else None
        )

    @loader.inline_everyone
    async def info_inline_handler(self, query: InlineQuery) -> dict:
        """Send 𝙰𝚞𝚝𝚑𝚘𝚛𝙲𝚑𝚎'𝚜  info"""
        m = {x: self._get_mark(x) for x in range(13)}
        btns = [
            [
                *([m[1]] if m[1] else []),
                *([m[2]] if m[2] else []),
                *([m[3]] if m[3] else []),
            ],
            [
                *([m[4]] if m[4] else []),
                *([m[5]] if m[5] else []),
                *([m[6]] if m[6] else []),
            ],
            [
                *([m[7]] if m[7] else []),
                *([m[8]] if m[8] else []),
                *([m[9]] if m[9] else []),
            ],
            [
                *([m[10]] if m[10] else []),
                *([m[11]] if m[11] else []),
                *([m[12]] if m[12] else []),
            ],
        ]
        msg_type = "message" if self.config["disable_inline_banner"] else "caption"
        return {
            "title": self.strings("send_info"),
            "description": self.strings("description"),
            msg_type: self._render_info(),
            self.config["custom_format"]: self.config["custom_banner"],
            "thumb": "https://imgur.com/Ze2TtW3",
            "reply_markup": btns,
        }

    @loader.unrestricted
    async def infocmd(self, message: Message):
        """Send bot info"""
        m = {x: self._get_mark(x) for x in range(13)}
        btns = [
            [
                *([m[1]] if m[1] else []),
                *([m[2]] if m[2] else []),
                *([m[3]] if m[3] else []),
            ],
            [
                *([m[4]] if m[4] else []),
                *([m[5]] if m[5] else []),
                *([m[6]] if m[6] else []),
            ],
            [
                *([m[7]] if m[7] else []),
                *([m[8]] if m[8] else []),
                *([m[9]] if m[9] else []),
            ],
            [
                *([m[10]] if m[10] else []),
                *([m[11]] if m[11] else []),
                *([m[12]] if m[12] else []),
            ],
        ]
        await self.inline.form(
            message=message,
            text=self._render_info(),
            reply_markup=btns,
            **{}
            if self.config["disable_banner"]
            else {self.config["custom_format"]: self.config["custom_banner"]}
        )
