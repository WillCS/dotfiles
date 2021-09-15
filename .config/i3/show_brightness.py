#!/usr/bin/python
import subprocess

result = subprocess.run(
    ["xbacklight", "-get"],
    stdout = subprocess.PIPE
).stdout.decode('utf-8')

brightness = round(float(result))
subprocess.run([
    "dunstify",
    "-t", "1000",
    "-h", "string:x-dunst-stack-tag:system_popup",
    f"Brightness [{brightness}%]",
    "-h", f"int:value:{brightness}",
])
