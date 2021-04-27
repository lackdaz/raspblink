import logging
from threading import Thread, Event
from typing import List, Optional, Callable
import time
from .base_classes import BaseThread

logger = logging.getLogger(__name__)


class LEDThread(BaseThread):
    thread_pool: List[Thread] = []

    def __init__(self):
        self.daemon_running: bool = False
        self._kill: Event = Event()
        self.thread: Optional[Thread] = None
        self.testy_test = 1

    def thread_daemon(self, callback: Callable, delay: float):
        """instance method to pulse indefinitely"""
        while True:
            callback()
            is_killed = self._kill.wait(delay)
            if is_killed:
                break

    def kill(self):
        self._kill.set()

    def start(self, callback: Callable, delay: float):
        self.thread = Thread(target=self.thread_daemon, args=[callback, delay])
        self.__class__.thread_pool.append(self.thread)
        self.daemon_running = True
        self.thread.start()

    def stop(self, exit_callback: Optional[Callable] = None):
        self.daemon_running = False
        thread_pool = self.__class__.thread_pool
        try:
            if self.thread:
                thread_pool.pop(thread_pool.index(self.thread))
                self.thread = None
        except:
            logger.error(f"threadpool could not pop thread")
        finally:
            logger.debug(f"popped thread off thread pool")
        if exit_callback:
            exit_callback()
