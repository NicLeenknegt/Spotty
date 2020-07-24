
import time
import queue
from resources.decorators.threading import run_on_thread

class ViewModel:
   
    @run_on_thread
    def get_devices(self, pipeline:queue):
        time.sleep(2)
        pipeline.put({ 'result':"wow" })
