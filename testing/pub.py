import struct
from subprocess import Popen, PIPE
import subprocess
# Note: This is acting as the autopilot

# TELEMETRY_STRUCT = struct.Struct(">f")   # INCOMING
COMMAND_STRUCT = struct.Struct(">f")         # OUTGOING

while 1:
    print(COMMAND_STRUCT.pack(float(10)))