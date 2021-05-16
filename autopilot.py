import sys
import struct
import ctypes

from time import sleep

# file1 = open("data.txt", 'w')
TELEMETRY_STRUCT = struct.Struct(">Hhffb31B")
COMMAND_STRUCT = struct.Struct(">fB3s")

## Command fake outputs
airspeed = ctypes.c_float(1.0)
drop = ctypes.c_uint8(1)
p1 = ctypes.c_char(1)
p2 = ctypes.c_char(1)
p3 = ctypes.c_char(1)
p = [p1, p2, p3]



# logging data for debugging
file1 = open("data.txt", 'w')
file1.write("The following data file is recording data from inside the autopilot function!")

drop = 1
while :
    tele = sys.stdin.buffer.read(44)
    # loop, x_err, wind0, wind1, y_err, lidar = TELEMETRY_STRUCT.unpack(tele)
    loop = str(TELEMETRY_STRUCT.unpack(tele)[0])

    file1.write(loop)
    file1.write("\n")
    # Write to command struct
    airspeed = 13.2256
    padding = bytes(1)

    sys.stdout.buffer.write(COMMAND_STRUCT.pack(airspeed, drop, padding))
    sys.stdout.buffer.flush()
    drop += 1
    if drop >250:
        drop = 1












## Functions to read and process data

def drop(iter):
    return 1 if iter%200==0 else 0

def Lidar(lidar_data):
    pass
