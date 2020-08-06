
import time
import queue
from resources.threading.ThreadingWrapper import ThreadingWrapper
from typing import Callable
import resources.GlobalVariables

class ViewModel:

    def __init__(self):
        self.reference = self
        resources.GlobalVariables.view_model_reference = self

