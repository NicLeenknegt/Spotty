
import time
import queue
from resources.decorators.threading import run_in_thread 
from resources.threading.ThreadingResult import ThreadingResult
from resources.patterns.observer.Observable import Observable
from view_models.ViewModel import ViewModel

class DeviceViewModel(ViewModel):

    def __init__(self):
        ViewModel.__init__(self)
        self.device_list = Observable(None)

    def get_devices_on_success(self,result:any) -> None:
        print(result.get_result())

    def get_devices_on_error(self,result:any) -> None:
        print("ERROR")

    @run_in_thread(get_devices_on_success, get_devices_on_error)
    def get_devices(self) -> dict:
        time.sleep(2)
        return {'result', "wow"}

    def set_observable(self, value):
        self.device_list.set(value)
