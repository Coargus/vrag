"""Prompt utility modules."""

from __future__ import annotations

from pathlib import Path


def prompt_loader(directory: Path | str, filename: str) -> any:
    """Prompt loader.

    Args:
        directory (str): Directory path.
        filename (str): Filename.

    Returns:
        any: Prompt object.
    """
    if isinstance(directory, str):
        directory = Path(directory)
    prompt_template_path = directory / filename

    with Path(prompt_template_path).open("r") as prompt_file:
        return prompt_file.read()
