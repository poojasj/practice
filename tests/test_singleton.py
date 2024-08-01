from practice.singleton import Singleton


def test_singleton():
    first = Singleton()
    second = Singleton()
    assert first is second
