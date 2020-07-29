
import time
import queue
from resources.decorators.threading import run_on_thread, run_in_thread 
from resources.patterns.observer.Observable import Observable

class ViewModel:

    def __init__(self):
        self.device_list = Observable(None)

    @run_on_thread
    def get_devices(self, pipeline:queue):
        time.sleep(2)
        pipeline.put({ 'result':"wow" })

    def get_class_reference(self) -> object:
        return self

    def get_devices_on_success(self,result:any) -> None:
        print(result)

    def get_devices_on_error(self,result:any) -> None:
        print("ERROR")

    @run_in_thread( get_class_reference() , get_devices_on_success, get_devices_on_error)
    def get_devices_v2(self) -> dict:
        time.sleep(2)
        return {'result', "wow"}

   # def thread_test(self):
   #     thread = ThreadingWrapper()
   #     thread.threading_target = self.get_devices
   #     thread.run()
   #     thread.join_thread()

    def set_observable(self, value):
        self.device_list.set(value)
