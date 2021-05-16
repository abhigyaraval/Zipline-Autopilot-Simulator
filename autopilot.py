"""
autopilot.py- Program to autopilot the Zipline autonomous vehicle in the prosperous land of Zipago
Author: Abhigya Raval
"""

import sys # sys module is used for communicate with the simulator in binary protocol
import struct # struct module is used to appropriate the format of incoming and outgoing communication
import time

# Functions to read and process data
def drop_package(iter):
    return 1 if iter%200==0 else 0

def Lidar(lidar_data):
    pass




# # file1 = open("data.txt", 'w')
TELEMETRY_STRUCT = struct.Struct(">Hhffb31B")
COMMAND_STRUCT = struct.Struct(">fB3s")
#
# ## Command fake outputs
# airspeed = ctypes.c_float(1.0)
# drop = ctypes.c_uint8(1)
# p1 = ctypes.c_char(1)
# p2 = ctypes.c_char(1)
# p3 = ctypes.c_char(1)
# p = [p1, p2, p3]
#


# logging data for debugging
# file1 = open("data.txt", 'w')
# file1.write("The following data file is recording data from inside the autopilot function!\n\n")
# file1 = open("data.txt", 'a')

iter = 1
while True:
    iter = iter +1
# for iter in range(1000000):
    # Reading from telemetry struct
    telemetry = sys.stdin.buffer.read(44)
    tele_data = TELEMETRY_STRUCT.unpack(telemetry)
    # loop, x_err, wind0, wind1, y_err, lidar = TELEMETRY_STRUCT.unpack(tele)
    # sim_time = tele_data[0]/1000
    # x_error = tele_data[1]
    # wind_x = tele_data[2]
    # wind_y = tele_data[3]
    # y_err = tele_data[4]
    # lidar = tele_data[5:37]
    print("Autopilot in loop#: ", iter)
    print(tele_data)
    print("\n")
    sys.stdin.buffer.flush()
    # time.sleep(1/60)

    # file1.write(str(tele_data))
    # file1.write("\n")
    # file1.write("sim_time: " + str(sim_time) + " seconds")
    # file1.write("x_error: " + str(x_error))
    # file1.writelines("Lidar dat: " + str(lidar))
    # file1.write("\n")
    #
#-------------------------------------------------------------------------------------------------------
    # Write to command struct
    # airspeed = 10.2256
    # padding = bytes(1)
    # drop = drop_function(iter)
    # sys.stdout.buffer.write(COMMAND_STRUCT.pack(airspeed, drop, padding))
    # sys.stdout.buffer.flush()
    if not sys.stdin.buffer.read():
        break   # If not data incoming, break out of the loop

# file1.close()

