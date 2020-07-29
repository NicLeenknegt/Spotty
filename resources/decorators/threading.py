
import queue
import threading
from resources.threading.ThreadingWrapper import ThreadingWrapper
from typing import Callable

def run_on_thread(f):
    def run(*k, **kw):
        t = threading.Thread(target=f, args=k, kwargs=kw)
        t.start()
        t.join()
    return run 

#def run_threading_wrapper(f):
#    def run(*k, **kw):
#        thread = ThreadingWrapper()
#        thread.threading_target = f
#        thread.run()
#    return run  

def run_in_thread(reference:object, on_success_listener:Callable[[any],None], on_error_listener:Callable[[any],None]):
    def wrapper(thread_target:Callable[[any],any]):
        def wrapper_w_args(*k, **kw):
            tw = ThreadingWrapper()
            tw.on_success_listener = on_success_listener
            tw.on_error_listener = on_error_listener
            tw.threading_target = thread_target 

            tw.start_thread(k)
            tw.finish_thread()
        return wrapper_w_args
    return wrapper
