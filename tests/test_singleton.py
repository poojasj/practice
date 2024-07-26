from practice.singleton import Singleton


def test_singleton():
    first = Singleton.get_instance()
    second = Singleton.get_instance()
    assert first is second