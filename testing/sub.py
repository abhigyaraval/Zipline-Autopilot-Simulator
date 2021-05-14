import struct
from subprocess import Popen, PIPE
import sys

# Note: This is acting as the simulator

COMMAND_STRUCT = struct.Struct(">d")         # INCOMING
TELEMETRY_STRUCT = struct.Struct(">d")   # OUTGOING
# print(COMMAND_STRUCT.size)
pilot = Popen(['python3', 'pub.py'], stdin=PIPE, stdout=PIPE)
file = open("data.txt", "w")
i = 1
while i < 1000:
    # print("Hello!")
    # i+=1

    # print(i)
    pilot.stdin.write(TELEMETRY_STRUCT.pack(float(1.2+i)))
    # pilot.stdin.write(TELEMETRY_STRUCT.pack(int(i)))
    cmd = pilot.stdout.read(COMMAND_STRUCT.size)
    print(sys.getsizeof(cmd))
    # pilot.stdin.flush()
    # print(COMMAND_STRUCT.size)
    cmd = COMMAND_STRUCT.unpack(cmd)
    file.write(cmd)
    pilot.stdout.flush()
    i += 1

file.close()
#
# TELEMETRY_STRUCT = struct.Struct(">Hhffb31B")
# COMMAND_STRUCT = struct.Struct(">fB3s")
#
# # pilot = Popen(['python3', 'pub.py'], stdin=PIPE, stdout=PIPE)
#
# while 1:
#     cmd = pilot.stdout.read(COMMAND_STRUCT.size)
#     var = COMM
#
#
