"""
Entry point for the setup. Calls the main function when the script is executed directly.
"""

import argparse

from telethon.sync import TelegramClient


def syncup(source: str, target: str) -> None:
    """
    Syncs data from the source platform to the target platform.

    Args:
        source (str): The source platform (e.g., 'telegram', 'discord').
        target (str): The target platform (e.g., 'twitter', 'telegram', 'discord').

    Raises:
        ValueError: If source or target is not in the allowed platforms.
    """
    allowed_platforms = ["twitter", "discord", "telegram"]
    source = source.lower()
    target = target.lower()
    if source not in allowed_platforms[1:]:
        raise ValueError(
            f"Invalid {source} platform: {source}. Allowed values are {allowed_platforms[1:]}."
        )
    if target not in allowed_platforms:
        raise ValueError(
            f"Invalid {target} platform: {target}. Allowed values are {allowed_platforms}."
        )

    if source == target:
        raise ValueError("Source and target platforms cannot be the same.")

    envionment_dict = dict()

    if source == allowed_platforms[0] or target == allowed_platforms[0]:
        envionment_dict["TWITTER_API_KEY"] = input("Enter twitter api key:").strip()
        envionment_dict["TWITTER_API_KEY_SECRET"] = input(
            "Enter twitter api key secret:"
        ).strip()
        envionment_dict["TWITTER_BEARER_TOKEN"] = input(
            "Enter twitter bearer token:"
        ).strip()
        envionment_dict["TWITTER_ACCESS_TOKEN"] = input(
            "Enter twitter access token(read and write permisisons):"
        ).strip()
        envionment_dict["TWITTER_ACCESS_TOKEN_SECRET"] = input(
            "Enter twitter access token secret(read and write permisisons):"
        ).strip()

    if source == allowed_platforms[1] or target == allowed_platforms[1]:
        envionment_dict["DISCORD_SERVER_ID"] = input(
            "Enter your discord server ID:"
        ).strip()
        envionment_dict["DISCORD_CHANNEL_ID"] = input(
            "Enter your discord channel ID:"
        ).strip()
        envionment_dict["DISCORD_TOKEN"] = input("Enter your discord token:").strip()
    if source == allowed_platforms[2] or target == allowed_platforms[2]:
        envionment_dict["TELEGRAM_API_HASH"] = input(
            "Enter your telegram api hash:"
        ).strip()
        envionment_dict["TELEGRAM_API_ID"] = input(
            "Enter your telegram api ID:"
        ).strip()
        envionment_dict["TELEGRAM_GROUP_NAME"] = input(
            "Enter your telegram group/user name:"
        ).strip()
        TelegramClient(
            "social_sycnup",
            envionment_dict["TELEGRAM_API_ID"],
            envionment_dict["TELEGRAM_API_HASH"],
        ).start()
    envionment_dict["SOURCE"] = source
    envionment_dict["TARGET"] = target
    print(
        "Please use these key value pairs for the respository secret in github: ",
        envionment_dict,
    )


def main() -> None:
    """
    The main entry point for the social_syncup command line tool.
    Parses command-line arguments and either starts interactive mode or syncs based on arguments.
    """
    parser = argparse.ArgumentParser(
        description="Sync your message on discord, twitter(write only) and telegram for free."
    )

    parser.add_argument(
        "start",
        nargs="?",
        default="start",
        help="Start the interactive terminal for setup",
    )
    parser.add_argument(
        "-s",
        "--source",
        help="Specify the source platform (e.g., telegram, discord, all)",
    )
    parser.add_argument(
        "-t",
        "--target",
        help="Specify the target platform (e.g., twitter, telegram, discord, all)",
    )

    args = parser.parse_args()

    try:
        if args.source and args.target:
            syncup(args.source, args.target)
        elif args.start.lower() == "start":
            source = input("Enter the source platform (telegram, discord): ")
            target = input("Enter the target platform (twitter, telegram, discord): ")
            syncup(source, target)
        else:
            parser.print_help()
    except ValueError as main_exc:
        parser.print_help()
        raise main_exc


if __name__ == "__main__":
    main()
