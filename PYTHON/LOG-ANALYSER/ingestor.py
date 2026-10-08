import json
import re
import datetime
from pathlib import Path

"""Designed to ingest logs from multiple sources and formats.
   Supports:
    - Apache/ HTTP access logs
    - Linux SSH
    - Generic text logs
    - JSON structured logs """

