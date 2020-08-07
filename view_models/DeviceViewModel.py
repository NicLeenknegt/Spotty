
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
        self.error_message = Observable(None)

    def get_devices_on_success(self,result:ThreadingResult) -> None:
        self.device_list.set(result.get_result())

    def get_devices_on_error(self,result:any) -> None:
        self.error_message.set(result.get_result())

    @run_in_thread(get_devices_on_success, get_devices_on_error)
    def get_devices(self) -> dict:
        time.sleep(2)
        return {'result', "wow"}
