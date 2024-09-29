"""
Starts of the script.
"""

import os
from dotenv import load_dotenv

from src import DiscordModule, TwitterModule, TelegramModule

load_dotenv()


def get_module(module_name: str):
    """
    Factory function to get the appropriate module instance.

    Parameters:
    module_name (str): The name of the module to get (twitter, discord, telegram).

    Returns:
    IOInterface: An instance of the requested module.

    Raises:
    ValueError: If the module_name is not recognized.
    """
    if module_name == "twitter":
        return TwitterModule()
    elif module_name == "discord":
        return DiscordModule()
    elif module_name == "telegram":
        return TelegramModule()
    else:
        raise ValueError(f"Unknown module: {module_name}")


def main(source_m: str, target_m: str) -> None:
    """
    Main processing starting point
    """
    if source_m == target_m:
        raise ValueError("Source and target cannot be the same.")
    if source_m == "twitter":
        raise ValueError("Source cannot be twitter, as twitter is \
                         write only as mentioned in the docs.")
    source_module = get_module(source_m)
    target_module = get_module(target_m)

    data = source_module.read()
    target_module.write(data)


if __name__ == "__main__":
    source = os.getenv("SOURCE", None)
    target = os.getenv("TARGET", None)
    main(source, target)
