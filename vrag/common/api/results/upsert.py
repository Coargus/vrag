import dataclasses


@dataclasses.dataclass
class UpsertResult:
    """UpsertResult Dataclass."""

    upsert_time: float
    number_of_vectors: int

    def __post_init__(self, **kwargs: any) -> None:
        """Post init method.

        Args:
        **kwargs (any): Additional arguments.
        """
        self.upsert_time = round(self.upsert_time, 3)
