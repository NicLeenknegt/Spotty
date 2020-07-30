
import time
import queue
from resources.decorators.threading import run_on_thread, run_in_thread 
from resources.threading.ThreadingResult import ThreadingResult
from resources.patterns.observer.Observable import Observable

class ViewModel:

    reference = None

    def __init__(self):
        self.device_list = Observable(None)
        reference = self

    def get_devices_on_success(self,result:any) -> None:
        print(result.get_result())

    def get_devices_on_error(self,result:any) -> None:
        print("ERROR")

    @run_in_thread( reference , get_devices_on_success, get_devices_on_error)
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
