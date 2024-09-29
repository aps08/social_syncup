"""
Writer Interface.
"""

from abc import ABC, abstractmethod


class Writer(ABC):
    """
    Abstract base class for writing data.

    This class should be inherited by any class that implements the write functionality.
    """

    @abstractmethod
    def write(self, data: list) -> None:
        """
        Writes data to the target.

        Parameters:
        data (str): The data to be written.

        This method should be overridden by subclasses to provide specific writing functionality.
        """
