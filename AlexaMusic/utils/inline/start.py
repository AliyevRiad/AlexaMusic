# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP, OWNER_ID
from AlexaMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["Kömək📚"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_["Kömək📚"], callback_data="settings_helper"),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["Kanal📤"], url=f"MediaMusicSupport"),
                InlineKeyboardButton(text=_["Support📬"], url=f"MediaMusicSupport"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["Kanal📤"], url=f"MediaMusicSupport")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text=_["Support📬"], url=f"MediaMusicSupport")]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [InlineKeyboardButton(text=_["Geri🔙"], callback_data="settings_back_helper")]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["Kanal📤"], url=f"MediaMusicSupport"),
                InlineKeyboardButton(text=_["Support 📬"], url=f"MediaMusicSupport"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["Kanal📤"], url=f"MediaMusicSupport")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text=_["Support📬"], url=f"MediaMusicSupport")]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["➕Məni Qrupuna Əlavə Et"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER_ID:
        buttons.append(
            [
                InlineKeyboardButton(text=_["Owner🧑‍💻"], user_id=OWNER_ID),
                InlineKeyboardButton(text=_["Developer🧑‍💻"], user_id=OWNER_ID),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(text=_["Developer👤"], user_id=OWNER_ID"),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(text=_["Owner👤"], user_id=OWNER_ID),
                ]
            )
    return buttons
