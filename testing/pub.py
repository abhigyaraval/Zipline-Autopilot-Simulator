import struct
from subprocess import Popen, PIPE
import subprocess
# Note: This is acting as the autopilot

TELEMETRY_STRUCT = struct.Struct("i")   # INCOMING
COMMAND_STRUCT = struct.Struct("i")         # OUTGOING

while 1:
    print(COMMAND_STRUCT.pack(int(10)))
    # print("Hello!")
    # var  = input()
    # var = TELEMETRY_STRUCT.unpack(var)
    # print(var)