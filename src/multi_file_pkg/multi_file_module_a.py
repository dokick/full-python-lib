"""Data class"""

from attrs import field, frozen, validators


@frozen
class SomeHashableDataClass:
    """Some hashable data class"""
    data: int = field(default=0)
    more_data: float = field(default=1, validator=[validators.gt(0)])
