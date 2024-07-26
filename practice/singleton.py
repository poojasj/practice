# TODO correct way to implement this will be @lru_cache(maxsize=None) ref:https://stackoverflow.com/a/73988733
class Singleton:
    instance = None

    def __init__(self, x) -> None:
        self.x = x

    @staticmethod
    def get_instance():
        if not Singleton.instance:
            Singleton.instance = Singleton(5)
        return Singleton.instance
