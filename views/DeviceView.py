
import queue
from view_models.ViewModel import ViewModel

class DeviceView:

    def __init__(self, view_model:ViewModel):
        self.view_model = view_model

    def show_device_table(self):
        pipeline = queue.Queue(maxsize=1)
        t = self.view_model.get_devices(pipeline)
        t.join()
        print(pipeline.get())
