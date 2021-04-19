__all__ = ["BasePWM", "BaseLED", "Singleton"]

from abc import ABC, abstractmethod
from typing import Set, List, Optional, Callable
from threading import Thread


class BasePWM(ABC):
    @abstractmethod
    def switch_on(self, intensity):
        pass

    @abstractmethod
    def switch_off(self):
        pass


class BaseLED(ABC):
    @abstractmethod
    def slow_on(self, period):
        pass

    @abstractmethod
    def slow_off(self, period):
        pass

    @abstractmethod
    def pulse(self, period, repeat):
        pass


class BaseThread(ABC):
    thread_pool: List[Thread] = []

    @abstractmethod
    def __init__(self):
        self.daemon_running: bool = False
        self.thread: Optional[Thread] = None

    @abstractmethod
    def thread_daemon(self, callback: Callable):
        pass

    @abstractmethod
    def start(self, callback: Callable):
        pass

    @abstractmethod
    def stop(self):
        pass


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]