"""Qdrant vectorizer module."""

from __future__ import annotations

import logging
import timeit
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from vrag.common.api.results import UpsertResult
from vrag.common.api.vector_document import VectorDocument
from vrag.retriever.qdrant import QdrantRetriever
from vrag.vectorizer import BaseVectorizer


class QdrantVectorizer(BaseVectorizer):
    """Qdrant Vectorizer class."""

    def __init__(self, client: QdrantClient, embedding_model: any) -> None:
        """Initialize QdrantVectorizer."""
        self.vectordb = client
        self.embedding_model = embedding_model

    def upsert(
        self,
        collection: str,
        vectors: list[VectorDocument],
        **kwargs: dict[str, any],
    ) -> UpsertResult:
        """Upsert vectors to Qdrant.

        Args:
            collection (str): Collection name.
            vectors (list[VectorDocument]): List of vectors to upsert.
            **kwargs (dict[str, any]): Additional arguments.
        """
        for vector in vectors:
            points = [
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector.embedding_vector,
                    payload=vector.metadata,
                )
            ]
        # Timing the upsert operation
        start_time = timeit.default_timer()
        self.vectordb.upsert(collection, points)
        elapsed_time = timeit.default_timer() - start_time
        logging.info(f"Time taken to execute upsert: {elapsed_time} seconds")
        return UpsertResult(
            upsert_time=elapsed_time, number_of_vectors=len(vectors)
        )

    def get_vector(
        self, vector_id: str | int, text: str, metadata: dict[str, str]
    ) -> VectorDocument:
        """Convert document to VectorDocument.

        Args:
            vector_id (str | int): Document ID.
            text (str): Document text.
            metadata (dict[str, str]): Document metadata.

        Returns:
            VectorDocument: Converted VectorDocument.
        """
        embedding_vector = self.embedding_model.vectorize(texts=text)
        return VectorDocument(
            id=vector_id,
            embedding_vector=embedding_vector.embedding_vector,
            metadata=metadata,
        )

    def as_retriever(self, **kwargs: any) -> QdrantRetriever:
        """Return retriever object."""
        return QdrantRetriever(
            client=self.vectordb, embedding_model=self.embedding_model
        )
