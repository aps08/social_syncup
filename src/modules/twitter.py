"""
Responsible for twitter module.
"""

import os
import tweepy
from tweepy.api import API
from tweepy.client import Client
from src.interfaces import Writer


class Creator:
    """
    Creates required objects for twitter API calls.
    """

    def get_client(self) -> Client:
        """
        Public function to create and return Client object.
        return:
            client: twitter client object.
        """
        try:
            client = tweepy.Client(
                bearer_token=os.environ.get("TWITTER_BEARER_TOKEN"),
                consumer_key=os.environ.get("TWITTER_API_KEY"),
                consumer_secret=os.environ.get("TWITTER_API_KEY_SECRET"),
                access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
                access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
            )
        except Exception as client_obj_err:
            raise client_obj_err
        return client

    def get_oauth(self) -> API:
        """
        Public function to create and return OAuth object.
        return:
            auth: twitter OAuth object.
        """
        try:
            auth = tweepy.OAuthHandler(
                consumer_key=os.environ.get("TWITTER_API_KEY"),
                consumer_secret=os.environ.get("TWITTER_API_KEY_SECRET"),
                access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
                access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
            )
            twitter_api = tweepy.API(auth)
        except Exception as oauth_obj_err:
            raise oauth_obj_err
        return twitter_api


class TwitterModule(Writer, Creator):
    """
    Module for handling reading from and writing to Twitter.
    """

    def __init__(self) -> None:
        """constructor"""
        Creator.__init__(self)
        self.__client = self.get_client()
        self.__oauth_api = self.get_oauth()

    def write(self, data: list) -> None:
        """
        Writes data to Twitter.

        Parameters:
        data (dict): The data to be written to Telegram.
        """
        for item in data:
            message, image = item.get("message", None), item.get("image", None)
            if message and image:
                media = self.__oauth_api.media_upload(image)
                self.__client.create_tweet(
                    text=message, media_ids=[media.media_id]
                )
            elif message and not image:
                self.__client.create_tweet(text=message)
            elif image and not message:
                media = self.__oauth_api.media_upload(image)
                self.__client.create_tweet(text=None, media_ids=[media.media_id])
