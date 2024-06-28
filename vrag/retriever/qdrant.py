"""Qdrant vectorizer module."""

from __future__ import annotations

from string import Template

from qdrant_client import QdrantClient

from vrag import prompt_module
from vrag.retriever import BaseRetriever


class QdrantRetriever(BaseRetriever):
    """Qdrant Vectorizer class."""

    def __init__(self, client: QdrantClient, embedding_model: any) -> None:
        """Initialize QdrantVectorizer."""
        self.vectordb = client
        self.embedding_model = embedding_model

    def retrieve(self, prompt: str, n_rank: int = 6, **kwargs: any) -> any:
        """Retrieve method.

        Args:
            prompt (str): Prompt to retrieve.
            n_rank (int): Number of results to return.
            **kwargs (any): Additional

        Returns:
            any: Search result.
        """
        collection_name = kwargs.get("collection_name")
        if collection_name:
            query_embedding = self.embedding_model.vectorize(prompt)
            search_result = self.vectordb.search(
                collection_name=collection_name,
                query_vector=query_embedding.embedding_vector,
                limit=n_rank,
            )
        else:
            err_msg = "Collection name not provided."
            raise ValueError(err_msg)
        return search_result

    def retrieve_as_prompt(
        self, prompt: str, n_rank: int = 6, **kwargs: any
    ) -> any:
        """Retrieve method.

        Args:
            prompt (str): Prompt to retrieve.
            n_rank (int): Number of results to return.
            **kwargs (any): Additional

        Returns:
            any: Search result.
        """
        collection_name = kwargs.get("collection_name")
        retrieval_results = self.retrieve(
            prompt=prompt,
            collection_name=collection_name,
            n_rank=n_rank,
        )
        retrieval_result_as_str = ""
        for rank, retrieval_result in enumerate(retrieval_results):
            contents = retrieval_result.payload.get("contents")
            retrieval_result_as_str += f"Rank {rank}: {contents}\n"

        return Template(prompt_module.RETRIEVER_AS_PROMPT).safe_substitute(
            n_rank=n_rank, retrieval_results=retrieval_result_as_str
        )
