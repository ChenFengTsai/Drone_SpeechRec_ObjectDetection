import sys

import configparser
from djitellopy import Tello

from object_detection import Object_Tracking


def main(drone):
    
    # todo: object dection to find (bottle)
    ot = Object_Tracking(drone)
    #ot.initialize_drone()
    ot.track_object()
    print('object tracking done')

if  __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    ip = config.get('wifi', 'ip')
    
    # initilize the drone
    drone = Tello(ip)
    #drone.connect()
    #drone.streamon()
    
    main(drone)