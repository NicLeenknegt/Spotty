
import time
import queue
from resources.decorators.threading import run_on_thread
from resources.patterns.observer.Observable import Observable

class ViewModel:

    def __init__(self):
        self.device_list = Observable(None)
   
    @run_on_thread
    def get_devices(self, pipeline:queue):
        time.sleep(2)
        pipeline.put({ 'result':"wow" })

    def set_observable(self, value):
        self.device_list.set(value)
