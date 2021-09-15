#!/usr/bin/python
import subprocess
import re

process_result = subprocess.run(
    ["amixer", "sget", "Master"],
    stdout = subprocess.PIPE
).stdout.decode('utf-8')

result = re.search("\[(\d+)\%\]", process_result)

if len(result.groups()) > 0:
    volume = round(float(result.groups()[0]))
    subprocess.run([
        "dunstify",
        "-t", "1000",
        "-h", "string:x-dunst-stack-tag:system_popup",
        f"Volume [{volume}%]",
        "-h", f"int:value:{volume}",
    ])
