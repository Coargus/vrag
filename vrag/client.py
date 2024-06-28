"""Vrag client module."""

from string import Template

from openai import OpenAI  # openai==1.2.0

from vrag import prompt_module
from vrag.retriever import BaseRetriever


class VragClient:
    """vrag client class."""

    def __init__(self, url: str, api_key: str, retriever=BaseRetriever) -> None:
        """Initialize vrag client.

        Args:
            url (str): URL.
            api_key (str): API Key

        """
        self.url = url
        self.api_key = api_key
        self.retriever = retriever

    def rag_request(
        self, prompt: str, collection_name: str, n_rank: int = 3
    ) -> any:
        """Request method.

        Args:
            prompt (str): Prompt to request.
            collection_name (str): Collection name.

        Returns:
            any: Request result.
        """
        retrieval_result_prompt = self.retriever.retrieve_as_prompt(
            prompt=prompt,
            collection_name=collection_name,
            n_rank=n_rank,
        )
        rag_system_prompt = prompt_module.RAG_SYSTEM_PROMPT_KO
        rag_user_prompt = Template(
            prompt_module.RAG_USER_PROMPT_KO
        ).safe_substitute(
            question=prompt, retrieval_results=retrieval_result_prompt
        )
        messages = [
            {"role": "system", "content": rag_system_prompt},
            {"role": "user", "content": rag_user_prompt},
        ]
        client = OpenAI(
            api_key="up_Qt0FNm0YXZyHIXkUmfnVu6kEhFNWs",
            base_url="https://api.upstage.ai/v1/solar",
        )
        stream = client.chat.completions.create(
            model="solar-1-mini-chat",
            messages=messages,
            stream=True,
        )
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
