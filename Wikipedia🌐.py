
__version__ = (1, 0, 0)

import logging
import wikipedia
from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class WikiMod(loader.Module):
    """Module for wikipedia search"""

    strings = {
        "name": "Wikipedia🌐",
        "answer": "🌐 <b>{0}</b><a href='{1}'>:</a>\n\n<i>{2}</i>\n\n{3}",
        "error": "❗️ <b>{0}</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "wiki_lang",
                "en",
                "Language of wikipedia",
                validator=loader.validators.Choice(["en", "uk"]),
            ),
        )

    async def client_ready(self, client, db):
        self._client = client

    async def wikicmd(self, message):
        """
        <text> - search in wikipedia
        """
        args = utils.get_args_raw(message)
        try:
            wikipedia.set_lang(self.config["wiki_lang"])
        except Exception:
            wikipedia.set_lang("en")

        try:
            page = wikipedia.page(args)
            await utils.answer(
                message,
                self.strings["answer"].format(
                    utils.escape_html(page.title),
                    page.images[0],
                    utils.escape_html(page.summary),
                    page.url,
                ),
            )
        except wikipedia.exceptions.DisambiguationError as e:
            await utils.answer(message, self.strings["error"].format(e))
        except wikipedia.exceptions.PageError as e:
            await utils.answer(message, self.strings["error"].format(e))