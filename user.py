"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  AKIMAXMOVIES <https://t.me/akimaxmovies>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

from config import Config
from logger import LOGGER
from pyrogram import Client
from pytgcalls import PyTgCalls

USER = Client(
    Config.SESSION,
    Config.API_ID,
    Config.API_HASH,
    plugins=dict(root="plugins.userbot")
    )
group_call = PyTgCalls(USER, cache_duration=180)


