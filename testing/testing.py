import sys
import struct


TELEMETRY_STRUCT = struct.Struct(">Hhffb31B")
# TELEMETRY_STRUCT = struct.Struct(">Hh")

loop_count =1
lidar_samples = [i for i in range(31)]
wind = [1.04543, 2.44533]
y_err = -18
x_err = 1088
TELEMETRY_STRUCT.pack(loop_count, x_err, wind[0], wind[1], y_err, *lidar_samples)
# TELEMETRY_STRUCT.pack(loop_count, x_err)

print(TELEMETRY_STRUCT)
print(TELEMETRY_STRUCT.size)

