#!/usr/bin/env python3

from subprocess import Popen, PIPE

rofi = Popen(
    args=[
        'rofi',
        '-dmenu',
        '-i',
        '-p',
        'Option'
    ],
    stdin=PIPE,
    stdout=PIPE
)

options="""shutdown
reboot
exit
lock
"""

(stdout, stderr) = rofi.communicate(input=options.encode('utf-8'))

if rofi.returncode == 1:
    exit()
else:
    print(stdout)