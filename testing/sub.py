import struct
from subprocess import Popen, PIPE

# Note: This is acting as the simulator

COMMAND_STRUCT = struct.Struct("i")         # INCOMING
TELEMETRY_STRUCT = struct.Struct("i")   # OUTGOING

pilot = Popen(['python3', 'pub.py'], stdin=PIPE, stdout=PIPE)
qA                              
i = 1
while i:
    # print("Hello!")
    # i+=1
    # print(i)
    cmd = pilot.stdout.read(COMMAND_STRUCT.size)
    # pilot.stdin.write(TELEMETRY_STRUCT.pack(float(10)))
    # pilot.stdin.flush()
    # print(COMMAND_STRUCT.size)
    cmd = COMMAND_STRUCT.unpack(cmd)
    print(cmd)
    pilot.stdout.flush()


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
