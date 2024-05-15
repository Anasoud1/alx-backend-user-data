#!/usr/bin/env python3
"""
filter_datum module
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}', f'{f}={redaction}{separator}',
                         message)
    return message