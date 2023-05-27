from djitellopy import Tello
import os
import argparse

from voice_detection import Voice_Detection
from gesture_detection import Gesture_Detection
from yolov5.object_detection import Object_Tracking
import configparser



def main(drone, ip, func):
    # *voice detection to fly*
    vd = Voice_Detection(drone)
    vd.fly_drones_voice()
    print('voice detection done')
    
    # *gesture detection to flip*
    if func == "gesture":
        gd = Gesture_Detection(drone, ip)
        gd.gesture_trigger()
        print('gesture detection done')
    
    # *object detection to find specific object*
    elif func == "object":
        object = "chair"
        ot = Object_Tracking(drone)
        ot.track_object(object)
        print('object tracking done')
    
    

if  __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--func', type=str, help='Function to trigger: voice, gesture, or object')
    args = parser.parse_args()
    
    config = configparser.ConfigParser()
    # Get the parent directory path
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    dir = os.path.join(parent_dir, '..','config.ini')
    config.read(dir)
    ip = config.get('wifi', 'ip')
    
    # initilize the drone
    drone = Tello(ip)
    drone.connect()
    drone.streamon()
    print(f"Battery life percentage: {drone.get_battery()}%")
    
    main(drone, ip, args.func)