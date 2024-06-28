"""Vectorization base class."""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vrag.common.api.vector_document import VectorDocument


class BaseVectorizer(abc.ABC):
    """Base Vectorizer class."""

    @abc.abstractmethod
    def upsert(
        self, collection: str, vectors: list[VectorDocument], **kwargs: any
    ) -> any:
        """Upsert method.

        Args:
            vectors (list[VectorDocument]): Vector to upsert.
            collection (str): Collection name.
            **kwargs (any): Additional arguments.
        """
        raise NotImplementedError
