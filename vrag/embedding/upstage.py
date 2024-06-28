import logging
import timeit

import requests

from vrag.common.api import Embedding
from vrag.embedding._base import EmbeddingModel

UPSTAGE_BASE_URL = "https://api.upstage.ai/v1/solar/embeddings"


class UpstageEmbedding(EmbeddingModel):
    """Upstage Embedding class."""

    def __init__(self, api_key: str, model: str) -> None:
        """Init method."""
        self.upstage_session = requests.Session()
        self._model = model
        self._headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        }

    def vectorize(self, texts: str) -> Embedding:
        """Vectorize text to embedding.

        Args:
            texts (str): Text to vectorize.
        """
        body = {
            "input": texts,
            "model": self._model,
        }
        start_time = timeit.default_timer()
        response_body = self.upstage_session.post(
            UPSTAGE_BASE_URL, headers=self._headers, json=body
        ).json()
        elapsed_time = timeit.default_timer() - start_time
        logging.info(f"Time taken to execute upsert: {elapsed_time} seconds")
        return Embedding(
            embedding_time=elapsed_time,
            embedding_vector=response_body["data"][0]["embedding"],
            text_length=len(texts),
        )
