"""
Responsible for discord module.
"""

import os
import json
from datetime import datetime, timedelta, timezone
import requests
from src.interfaces import Reader, Writer


class DiscordModule(Reader, Writer):
    """
    Module for handling reading from and writing to Discord.

    This class implements the IOInterface to provide specific functionality for Discord.
    """

    def __init__(self) -> None:
        self.__token = os.environ.get("DISCORD_TOKEN")
        self.__url = "https://discord.com/api/v10/"
        self.__headers = {"authorization": f"Bot {self.__token}"}

    def read(self) -> list:
        """
        Reads data from Discord.

        Returns:
        str: A string indicating that data is being read from Discord.
        """
        fetched_data = []
        channel_id = os.environ.get("DISCORD_CHANNEL_ID")
        api_url = self.__url + "channels/" + channel_id + "/messages?limit=30"
        response = requests.get(api_url, headers=self.__headers, timeout=5000)
        if response.ok:
            date_time = datetime.now(timezone.utc) - timedelta(hours=1.0)
            messages = [
                item
                for item in json.loads(response.text)
                if datetime.fromisoformat(item["timestamp"]) > date_time
            ]
            for message in messages:
                fetched_message, image_path = None, None
                if message["attachments"]:
                    image_path = message["attachments"][0]["filename"]
                    cdn_url = message["attachments"][0]["url"]
                    with open(message["attachments"][0]["filename"], "wb") as file:
                        response = requests.get(cdn_url, stream=True, timeout=5000)
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                file.write(chunk)
                if message["content"]:
                    fetched_message = message["content"]
                if fetched_message or image_path:
                    fetched_data.append(
                        {"message": fetched_message, "image": image_path}
                    )
        return fetched_data

    def write(self, data: list) -> None:
        """
        Writes data to Discord.

        Parameters:
        data (str): The data to be written to Discord.
        """
        channel_id = os.environ.get("DISCORD_CHANNEL_ID")
        api_url = self.__url + "channels/" + channel_id + "/messages"
        for item in data:
            message, image = item.get("message", None), item.get("image", None)
            if message and image:
                files = {"file": (image.split("/")[1], open(image, "rb"))}
                requests.post(
                    api_url,
                    data={"content": message},
                    headers=self.__headers,
                    files=files,
                    timeout=5000,
                )
            elif message and not image:
                requests.post(
                    api_url,
                    data={"content": message},
                    headers=self.__headers,
                    timeout=5000,
                )
            elif image and not message:
                files = {"file": image}
                requests.post(
                    api_url, headers=self.__headers, files=files, timeout=5000
                )
