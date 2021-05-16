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



while True:
    tele = sys.stdin.read()
    time, x_err, wind_x, wind_y, y_err, lidar = TELEMETRY_STRUCT.unpack(tele)

    # cmd = sys.stdout.write(COMMAND_STRUCT.pack(airspeed, drop, ctypes.c_uint8(1)))
