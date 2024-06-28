"""Vectorization base class."""

from __future__ import annotations

import abc


class BaseRetriever(abc.ABC):
    """Base Vectorizer class."""

    @abc.abstractmethod
    def retrieve(self, prompt: str, n_rank: int, **kwargs: any) -> any:
        """Retrieve method.

        Args:
            prompt (str): Prompt to retrieve.
            n_rank (int): Number of results to return.
            **kwargs (any): Additional arguments.
        """
        raise NotImplementedError
