import struct
import subprocess
import sys
# 
# # Note: This is acting as the simulator

# Structs used to pack/unpack the API messages (> meaning Big Endian)
# milliseconds [2 bytes]
# wind_x [4 bytes]
# wind_y [4 bytes]
# recovery_x error [2 bytes]
# recovery_y error [1 byte]
# 31 lidar samples [31 bytes]
# TELEMETRY_STRUCT = struct.Struct(">f")
# COMMAND_STRUCT = struct.Struct(">f")
import time

TELEMETRY_STRUCT = struct.Struct(">Hhffb31B")
COMMAND_STRUCT = struct.Struct(">fB3s")



pilot = subprocess.Popen(['python3', 'pub.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
loop_count = 0  # To count iterations to compute the telemetry timestamp
result = None
########## This is in the main loop
while result != "Crashed":
    try:
        lidar_samples = [i+i*4 for i in range(31)]
        wind = [1.04543, 2.44533]
        y_err = -18
        x_err = 1088
        pilot.stdin.write(TELEMETRY_STRUCT.pack(int(loop_count),
                                                x_err,
                                                wind[0],
                                                wind[1],
                                                y_err,
                                            *lidar_samples))
        pilot.stdin.flush()
        loop_count += 1
        if loop_count>10000:
            loop_count=0

        cmd = pilot.stdout.read(COMMAND_STRUCT.size)
        # print("length of cmd: ", len(cmd))
        # print("length of COMMAND_STRUCT: ", COMMAND_STRUCT.size)
        if len(cmd) != COMMAND_STRUCT.size:
            result = "Crashed"  # The pilot process must have exited
            break
        lateral_airspeed_input, drop_package_commanded_byte, _ = COMMAND_STRUCT.unpack(cmd)
        print("Main: " + str(loop_count))
        print("Inner: ", drop_package_commanded_byte)
        # print("Com[1]: ", drop_package_commanded_byte)
        # print("Comm[2]: ", _)
        # time.sleep(1/60)
    except KeyboardInterrupt:
        print("Exiting program. Killing subprocess...")
        # pilot.kill()
        pilot.stdin.close()
        pilot.stdout.close()
        # pilot.wait()
        print("Subprocess killed. Exiting program...")

## Outside loop
# pilot.stdin.close()
# pilot.stdout.close()
# pilot.wait()