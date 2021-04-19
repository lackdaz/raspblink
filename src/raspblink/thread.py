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

    def thread_daemon(self, callback: Callable):
        """instance method to pulse indefinitely"""
        while True:
            # if not self.daemon_running:
            # break
            callback()
            is_killed = self._kill.wait()
            if is_killed:
                break

    def start(self, callback: Callable):
        self.thread = Thread(target=self.thread_daemon, args=[callback])
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
