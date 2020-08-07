
import queue
import threading
from typing import Callable
from resources.threading.ThreadingResult import ThreadingResult

class ThreadingWrapper:
    
    def __init__(self):
        self.threading_target:Callable[[any],any] 
        self.on_success_listener:Callable[[any], None]
        self.on_error_listener:Callable[[any], None]
        self.pipeline = queue.Queue(maxsize=1)
        self.thread = None
        self.reference = None

    def run_on_thread(self, *args):
        result:ThreadingResult = ThreadingResult()
        try:
            return_value:any = self.threading_target(args)
            result.set_ok()
            result.set_result(return_value)
        except Exception as e:
            result.set_error()
            result.set_result(e)
        finally:
            self.pipeline.put(result)

    def start_thread(self, *args):
        self.thread = threading.Thread(target=self.run_on_thread(), args=args)
        self.thread.start()

    def finish_thread(self):
        result:ThreadingResult = self.pipeline.get()
        self.thread.join()
        if result.is_ok(): 
            self.on_success_listener(self.reference, result)
        else:
            self.on_error_listener(self.reference, result)
