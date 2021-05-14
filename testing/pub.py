import struct
# from subprocess import Popen, PIPE
# import subprocess
import sys

# Note: This is acting as the autopilot

TELEMETRY_STRUCT = struct.Struct(">d")   # INCOMING
COMMAND_STRUCT = struct.Struct(">d")         # OUTGOING

while 1:
    incoming = sys.stdout.read(TELEMETRY_STRUCT.size)
    incoming = TELEMETRY_STRUCT.unpack(incoming)

    COMMAND_STRUCT.pack(incoming)
    sys.stdin.write(COMMAND_STRUCT)
