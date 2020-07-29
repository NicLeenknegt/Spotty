
from resources.threading.ThreadingStatus import ThreadingStatus

class ThreadingResult:

    def __init__(self):
        self.result:any = None
        self.status:ThreadingStatus = ThreadingStatus.UNDEFINED

    def is_ok(self) -> bool:
        return self.status == ThreadingStatus.OK

    def get_result(self) -> any:
        return self.result

    def set_result(self,result:any) -> None:
        self.result = result

    def set_ok(self) -> None:
        self.status = ThreadingStatus.OK

    def set_error(self) -> None:
        self.status = ThreadingStatus.ERROR
