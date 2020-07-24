
import threading

def run_on_thread(f):
    def run(*k, **kw):
        t = threading.Thread(target=f, args=k, kwargs=kw)
        t.start()
        return t
    return run 
