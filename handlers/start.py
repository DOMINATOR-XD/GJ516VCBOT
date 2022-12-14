import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CZp7eIAACZyJjThL0sfPlWyCJHXo2OfIXJHC3LwACdAYAArJscVY0KNBsR3kYDh4E")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()}Â , ð¥\n\n
à¹ This is [{bn}](t.me/{bu}) ,Â  !
â» The most Powerful telegram music  bot with some awesome and useful features.

ââââââââââââââââââ
à¹  All of my command can be used with My command handle : ( / . â¢ $ ^ ~ + * ? )
â» Made ð¤ by : [â¤ââ¥â ð¤ð£ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê ê Â¤âà¹âà£§à£§à£§à£§à£§à£§à£§à£§à£§à£§ð£ê ê ð²­ð²­ð²­ð¦âââð¤Òð©â£âN1xä¹DÃLLðªââ£ââ¤ï¸ðªââ£âð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­ð²­](https://t.me/N1xDOLL) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "âÂ AddÂ meÂ toÂ yourÂ Group", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "ð¨ Channel ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "ð¨ Support ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "ð¤ Bot Owner ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "ð¨âð» Developer ", url=f"https://t.me/N1xDOLL"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "â Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "ð¡ Git repo", url="https://t.me/Dollx_spambot"
                    )]
            ]
       ),
    )

