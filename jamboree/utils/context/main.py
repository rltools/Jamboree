
from loguru import logger
import maya
from crayons import magenta
from contextlib import ContextDecorator, contextmanager
from contextlib import contextmanager

class timecontext(ContextDecorator):
    def __enter__(self):
        self.start = maya.now()._epoch
        return self

    def __exit__(self, *exc):
        self.end = maya.now()._epoch
        delta = self.end - self.start
        print(f"It took {delta}ms")
        return False


class example_space(ContextDecorator):
    def __init__(self, name) -> None:
        self.name = name
        self.is_pass = True
        self.start = maya.now()._epoch
    
    def __enter__(self):
        logger.info(f"------------------------------------ Starting an Example: {magenta(self.name, bold=True)} --------------------------------------")
        return self
    
    def failed(self):
        self.is_pass = False

    def __exit__(self, type, value, traceback):
        self.end = maya.now()._epoch
        delta = self.end - self.start
        if value is not None or self.is_pass == False:
            logger.error("----------------------------------------- Example didn't pass --------------------------------------------")
        else:
            logger.success("------------------------------------------ Example did pass ----------------------------------------------")
        logger.info(f"It took {delta}ms")
        return False

if __name__ == "__main__":
    with example_space("Printing") as example:
        print("Don't want to kill my vibe")
        # example.failed()