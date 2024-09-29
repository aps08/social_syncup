"""
Reader Interface.
"""

from abc import ABC, abstractmethod


class Reader(ABC):
    """
    Abstract base class for reading data.

    This class should be inherited by any class that implements the read functionality.
    """

    @abstractmethod
    def read(self) -> list:
        """
        Reads data from the source.

        This method should be overridden by subclasses to provide specific reading functionality.
        """
