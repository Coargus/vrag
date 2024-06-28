import dataclasses


@dataclasses.dataclass
class Embedding:
    """Embedding Dataclass."""

    embedding_time: float
    embedding_vector: list[float]
    text_length: int

    def __post_init__(self, **kwargs: any) -> None:
        """Post init method.

        Args:
        **kwargs (any): Additional arguments.
        """
        self.embedding_time = round(self.embedding_time, 3)
