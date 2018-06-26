#!/usr/bin/env python2.7

import subprocess
from threading import Thread

def _execute(filename):
    p = subprocess.Popen('./'+filename, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()

    print "Command output : ", output
    print "Command exit status/return code : ", p_status

def execute(filename):
    thread = Thread(target = _execute, args = [filename])
    thread.start()
    thread.join()

execute("test.py")
