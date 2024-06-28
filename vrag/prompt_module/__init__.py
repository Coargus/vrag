"""Prompt module for Vrag."""

from pathlib import Path

from .utility import prompt_loader

prompt_root = Path(__file__).parent
RETRIEVER_AS_PROMPT = prompt_loader(
    directory=prompt_root / "templates", filename="retriever_as_prompt.txt"
)
RAG_SYSTEM_PROMPT_KO = prompt_loader(
    directory=prompt_root / "templates", filename="rag_system_prompt_ko.txt"
)
RAG_USER_PROMPT_KO = prompt_loader(
    directory=prompt_root / "templates", filename="rag_user_prompt_ko.txt"
)
