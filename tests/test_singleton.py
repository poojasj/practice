from practice.singleton import Singleton


def test_singleton():
    first = Singleton(1)
    second = Singleton(1)
    assert first is second
