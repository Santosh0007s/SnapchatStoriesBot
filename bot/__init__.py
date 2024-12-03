import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID" "22624627"))
    API_HASH = os.environ.get("API_HASH" "361cbca2db6bb5cba3a0a8b8f8f31dfa")
    BOT_TOKEN = os.environ.get("BOT_TOKEN" "8178396198:AAGA3zTFZbJSgO3o1Noda6XWz8LVEMsi1x8")
    BOT_USERNAME = os.environ.get("BOT_USERNAME" "snapchatstories_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
