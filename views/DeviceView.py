
import queue, sys
from view_models.ViewModel import ViewModel
from views.MainView import MainView

class DeviceView(MainView):

    def on_device_list_listener(self,value):
        self.stop_loading_animation()
        print("OBSERVER: " + str(value), flush=True)

    def on_error_listener(self, value:any):
        self.stop_loading_animation()
        print("ERROR: " + str(value), flush = True)

    def __init__(self, view_model:ViewModel):
        super().__init__()
        self.view_model = view_model
        self.view_model.device_list.observe(self.on_device_list_listener)
        self.view_model.error_message.observe(self.on_error_listener)

    def show_device_table(self):
        self.start_loading_animation()
        self.view_model.get_devices()
