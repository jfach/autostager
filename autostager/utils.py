import errno
import os

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            print "path exists"
            pass
        else:
            raise

art = """
    ___    __  __ ______ ____  _____ ______ ___    ______ ______ ____ 
   /   |  / / / //_  __// __ \/ ___//_  __//   |  / ____// ____// _ _\\
  / /| | / / / /  / /  / / / /\__ \  / /  / /| | / / __ / __/  / /_/ /
 / ___ |/ /_/ /  / /  / /_/ /___/ / / /  / ___ |/ /_/ // /___ / _, _/ 
/_/  |_|\____/  /_/   \____//____/ /_/  /_/  |_|\____//_____//_/ |_|
"""

