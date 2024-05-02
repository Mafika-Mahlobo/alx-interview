#!/usr/bin/python3
"""
Log parsing Script
"""

import sys
import re

pattern = pattern = (
    r"(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] "
    r"\"GET /projects/260 HTTP/1\.1\" (\d{3}) (\d+)"
    )
count = 0
total_file_size = 0
status_code_count = {200: 0,
                     301: 0,
                     400: 0,
                     401: 0,
                     403: 0,
                     404: 0,
                     405: 0,
                     500: 0
                     }
file_size = 0
status_code = 0
code_count = 0

try:
    for line in sys.stdin:

        match = re.match(pattern, line)

        if (match):
            file_size = int(match.group(4))
            status_code = int(match.group(3))

            total_file_size += file_size
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            count += 1

            if (count % 10 == 0):
                print(f"File size: {total_file_size}")
                for code in sorted(status_code_count.keys()):
                    code_count = status_code_count[code]
                    if code_count > 0:
                        print(f"{code}: {code_count}")

except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        code_count = status_code_count[code]
        if code_count > 0:
            print(f"{code}: {code_count}")
    sys.exit(0)
