
import queue
from view_models.ViewModel import ViewModel

class DeviceView:

    def on_change_listener(self,value):
        print("OBSERVER: " + value)

    def __init__(self, view_model:ViewModel):
        self.view_model = view_model
        self.view_model.device_list.observe(self.on_change_listener)

    def observer(self):
        self.view_model.set_observable("check")

    def show_device_table(self):
        #pipeline = queue.Queue(maxsize=1)
        self.view_model.get_devices()
