"""
autopilot.py- Program to autopilot the Zipline autonomous vehicle in the prosperous land of Zipago
Author: Abhigya Raval
"""
import random
import sys # sys module is used for communicate with the simulator in binary protocol
import struct # struct module is used to appropriate the format of incoming and outgoing communication

class vehicle():
    def __init__(self, wind_x):
        self.vx = 30 + wind_x
        self.vy = None
        self.v = 
        self.distance_from_recovery = None
        self.drop_it = 0

    def move_toward(self):
        pass

    def move_away(self):
        pass

    def classify(self):
        """
        scan lidar:
            if score in a range high enough, object detected
        object = tree if many points
        :return:
        """
        pass

    def desired_direction(self):
        """
        Change velocity vectors based on the angle that you want to go to
        current v = sqrt(self.vx^2 + self.vy^2)
        :return:
        """

    def distance_to_site(self):
        pass

    def velocity_vector(self):
        pass

    def drop_it(self):
        pass




# Helper functions

def read_telemetry(tele):
    data = TELEMETRY_STRUCT.unpack(tele)
    #return sim_time, x_err, wind_x, wind_y, y_err, lidar
    return data[0], data[1], data[2], data[3], data[4], data[5:37]


def drop_package(iter):
    return 1 if iter%20000==0 else 0


def lidar(lidar_data):
    pass





TELEMETRY_STRUCT = struct.Struct(">Hhffb31B")
COMMAND_STRUCT = struct.Struct(">fB3s")

# logging data for debugging
file1 = open("data.txt", 'w')

is_data_coming = True
# drop = 1
while is_data_coming:
    tele = sys.stdin.buffer.read(44)
    if len(tele) != TELEMETRY_STRUCT.size:
        is_data_coming = False
        break

    # data = TELEMETRY_STRUCT.unpack(tele)
    SIM_TIME, X_ERR, WIND_X, WIND_Y, Y_ERR, LIDAR_DATA = read_telemetry(tele)

    # Write to command struct
    airspeed = -WIND_Y
    drop = drop_package(int(SIM_TIME))
    padding = bytes(1)

    sys.stdout.buffer.write(COMMAND_STRUCT.pack(airspeed, drop, padding))
    sys.stdout.buffer.flush()


sys.stdin.close()
sys.stdout.close()
# file1.close()


