import pyautogui as pag
import subprocess
import time

exe_path = "vpnplanet.exe"

subprocess.Popen([exe_path])

actions = [
    (611,528,4),
    (611,528,2),
    (611,528,2),
    (611,528,2),
    (611,528,2),
    (611,528,2),
    (625,371,36),
    (626,531,5),
    (500,531,26),
    (427,479,12),
    (629,434,6),
    (856,156,36),
]

for x, y, duration in actions:
    pag.click(x, y, duration=duration)


# this is the application 
# Version 101.20.0.3 All copy rights editin



