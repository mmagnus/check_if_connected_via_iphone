#!/usr/bin/env python

import subprocess

def execute(cmd):
    o = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return o.stdout.read().strip(), o.stdout.read().strip()

def check_status_of_iphone_usb():
    """Check status of iphone USB.

    If 'status: active' is in an output of ifconfig en4

    Returns:

       bool: True if connected, otherwise return False.
    """
    output, error = execute('ifconfig en4')
    if 'status: active' in output and not error:
        return True
    else:
        return False
    
# main
if __name__ == '__main__':
    print check_status_of_iphone_usb()
    
