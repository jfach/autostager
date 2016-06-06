import errno
import os
import signal
from git_timeout import GitTimeout

class timeout:

    def __init__(self, seconds, error_message=os.strerror(errno.ETIME)):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise GitTimeout(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)

