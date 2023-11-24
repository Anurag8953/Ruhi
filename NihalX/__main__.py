import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from NihalX import LOGGER, app, userbot
from NihalX.core.call import Nihal
from NihalX.plugins import ALL_MODULES
from NihalX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("NihalX").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("NihalX").warning(
            "Spotify Client Id & Secret not added, Chutiya Saala ek itni simple cheej nahi laa paaya."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NihalX.plugins" + all_module)
    LOGGER("NihalX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Nihal.start()
    try:
        await Nihal.stream_call(
            "https://telegra.ph/file/8d5db123638c2f6bb6ce4.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("NihalX").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Nihal.decorators()
    LOGGER("NihalX").info("Music Bot Started Successfully, Now Gib your girlfriend chumt to @MR_CUTE_X")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("NihalX").info("Stopping Music Bot, Bhakk Bhosdike (Gaand Maraa Tu)")
