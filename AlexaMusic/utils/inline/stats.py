# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AlexaMusic import app


def back_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["Geri🔙"],
                    callback_data="TOPMARKUPGET",
                ),
                InlineKeyboardButton(
                    text=_["Bağla🔚"],
                    callback_data="close",
                ),
            ],
        ]
    )


def overallback_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["Geri🔚"],
                    callback_data="GlobalStats",
                ),
                InlineKeyboardButton(
                    text=_["Bağla🔚"],
                    callback_data="close",
                ),
            ],
        ]
    )


def get_stats_markup(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["Bağla🔚"],
            callback_data="close",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["Sudo"],
            callback_data="bot_stats_sudo g",
        ),
        InlineKeyboardButton(
            text=_["Bağla🔚"],
            callback_data="close",
        ),
    ]
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SA_B_7"],
                    callback_data="TOPMARKUPGET",
                )
            ],
            [
                InlineKeyboardButton(
                    text=_["Stat"],
                    url=f"https://t.me/{app.username}?start=stats",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_5"],
                    callback_data="TopOverall g",
                ),
            ],
            sudo if status else not_sudo,
        ]
    )


def stats_buttons(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["SA_B_5"],
            callback_data="TopOverall s",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_8"],
            callback_data="bot_stats_sudo s",
        ),
        InlineKeyboardButton(
            text=_["SA_B_5"],
            callback_data="TopOverall s",
        ),
    ]
    return InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def back_stats_buttons(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GETSTATS",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def top_ten_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SA_B_2"],
                    callback_data="GetStatsNow Tracks",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_1"],
                    callback_data="GetStatsNow Chats",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["SA_B_3"],
                    callback_data="GetStatsNow Users",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_4"],
                    callback_data="GetStatsNow Here",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GlobalStats",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
