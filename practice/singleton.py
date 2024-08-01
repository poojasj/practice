from functools import lru_cache


@lru_cache(maxsize=None)
class Singleton:
    def __init__(self, x) -> None:
        self.x = x
