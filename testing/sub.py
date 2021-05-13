import struct
from subprocess import Popen, PIPE

# Note: This is acting as the simulator

COMMAND_STRUCT = struct.Struct(">f")         # INCOMING
# TELEMETRY_STRUCT = struct.Struct(">f")   # OUTGOING

pilot = Popen(['python3', 'pub.py'], stdin=PIPE, stdout=PIPE)

while 1:
    cmd = pilot.stdout.read(COMMAND_STRUCT.size)
    var = COMMAND_STRUCT.unpack(cmd)