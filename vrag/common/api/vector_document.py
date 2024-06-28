import dataclasses


@dataclasses.dataclass
class VectorDocument:
    """VectorDocument Dataclass."""

    id: str
    embedding_vector: list[float]
    metadata: dict[str, str]

    def __post_init__(self, **kwargs: any) -> None:
        """Post init method.

        Args:
        **kwargs (any): Additional arguments.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
