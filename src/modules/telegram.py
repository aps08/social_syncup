"""
Responsible for telegram module.
"""

import os
from datetime import datetime, timedelta, timezone
from telethon.sync import TelegramClient
from src.interfaces import Reader, Writer


class TelegramModule(Reader, Writer):
    """
    Module for handling reading from and writing to Telegram.

    This class implements the IOInterface to provide specific functionality for Telegram.
    """

    def __init__(self) -> None:
        self.__client = TelegramClient(
            "social_sycnup",
            os.environ.get("TELEGRAM_API_ID"),
            os.environ.get("TELEGRAM_API_HASH"),
        ).start()
        self.__group = os.environ.get("TELEGRAM_GROUP_NAME")

    def read(self) -> list:
        """
        Reads data from Telegram.

        Returns:
        list: A list of dictionary indicating that data is being read from Telegram.
        """
        fetched_data = []
        date_time = datetime.now(timezone.utc) - timedelta(hours=1.0)
        messages = self.__client.iter_messages(
            entity=self.__group,
            offset_date=date_time,
            reverse=True,
        )
        for message in messages:
            fetched_message, image_path = None, None
            current_timestamp = datetime.now().strftime("%Y%d%m_%H%M%S_%f")
            export = "media/" + current_timestamp
            if message.reply_to:
                continue
            if message.photo and message.message:
                image_path = self.__client.download_media(message, export)
                fetched_message = message.message
            elif message.photo and not message.message:
                image_path = self.__client.download_media(message, export)
            elif message.message and not message.photo:
                fetched_message = message.message
            if image_path and "\\" in image_path:
                image_path = image_path.replace("\\", "/")
            if fetched_message or image_path:
                fetched_data.append({"message": fetched_message, "image": image_path})
        return fetched_data

    def write(self, data: list) -> None:
        """
        Writes data to Telegram.

        Parameters:
        data (dict): The data to be written to Telegram.
        """
        for item in data:
            message, image = item.get("message", None), item.get("image", None)
            self.__client.send_message(entity=self.__group, message=message, file=image)
