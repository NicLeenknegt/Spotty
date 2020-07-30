
import time
import queue
from resources.threading.ThreadingWrapper import ThreadingWrapper
from typing import Callable

class ViewModel:

    def __init__(self):
        self.reference = self

    def run_async(self, on_success_listener:Callable[[any],None], on_error_listener:Callable[[any],None]):
        def wrapper(thread_target:Callable[[any],any]):
            def wrapper_w_args(*k, **kw):
                tw = ThreadingWrapper()
                tw.on_success_listener = on_success_listener
                tw.on_error_listener = on_error_listener
                tw.threading_target = thread_target 
                tw.reference = self 

                tw.start_thread(k)
                tw.finish_thread()
            return wrapper_w_args
        return wrapper
