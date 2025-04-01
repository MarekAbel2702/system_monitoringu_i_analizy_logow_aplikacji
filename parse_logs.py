import re
from datetime import datetime

def parse_log_line(line):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)'
    match = re.match(pattern, line)
    if match:
        log_time_str = match.group(1)
        level = match.group(2)
        message = match.group(3)

        log_time = datetime.strptime(log_time_str, "%Y-%m-%d %H:%M:%S")
        return (log_time, level, message)
    else:
        return None