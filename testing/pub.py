import sys
import struct
# Note: This is acting as the autopilot

TELEMETRY_STRUCT = struct.Struct(">Hhffb31B")
COMMAND_STRUCT = struct.Struct(">fB3s")
file1 = open("data.txt", 'w')
drop = 1
inn_loop = 1.0
while True:
    try:
        tele = sys.stdin.buffer.read(44)
        # loop, x_err, wind0, wind1, y_err, lidar = TELEMETRY_STRUCT.unpack(tele)
        loop = str(TELEMETRY_STRUCT.unpack(tele)[0])

        file1.write(loop)
        file1.write("\n")
        # Write to command struct

        airspeed = drop

        padding = bytes(1)

        sys.stdout.buffer.write(COMMAND_STRUCT.pack(airspeed, drop, padding))
        sys.stdout.buffer.flush()
        drop += 1
        if drop >250:
            drop = 1
        inn_loop += 1
        if inn_loop > 10000:
            inn_loop=0.0
    except:
        sys.stdin.close()
        sys.stdout.close()
        file1.close()
#
# for i in range(30):
#     text = sys.stdin.readline()
#     # file1.write(process1.stdout.read())
#     print(text)
#     print("return val: ", sys.stdin)
#

