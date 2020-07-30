
import time
import queue
from resources.threading.ThreadingWrapper import ThreadingWrapper
from typing import Callable

class ViewModel:

    def __init__(self):
        self.reference = self
        global view_model_reference 
        view_model_reference = self

