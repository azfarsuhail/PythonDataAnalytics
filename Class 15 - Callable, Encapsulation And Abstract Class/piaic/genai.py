import time
from typing import Any

class executiontime:

    def __init__(self , func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = self.func(*args,**kwargs)
        end = time.perf_counter()
        print( f" {self.func}")