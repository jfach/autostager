from __future__ import print_function
import os
import sys
import syslog
import urllib
import datetime

def log(msg, level = syslog.LOG_INFO):
    msg = safe(msg)
    if os.environ.get('debug'):
        debugmsg = '{0} {1}'.format(datetime.datetime.now(), msg)
        print(debugmsg, file=sys.stderr)
    syslog.openlog('Autostager', syslog.LOG_PID, syslog.LOG_LOCAL0)
    syslog.syslog(level, msg)


def safe(str):
    return urllib.unquote_plus(str)
